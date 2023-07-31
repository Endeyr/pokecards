from pokemontcgsdk import Card as getCard, RestClient, Set as getSet
from django.core.management.base import BaseCommand
from ...models import *
from my_secrets import secrets
from datetime import datetime

API_KEY = secrets.API_KEY

RestClient.configure(API_KEY)


def format_date(date_string):
    date = datetime.strptime(date_string, "%Y/%m/%d")
    formatted_date = date.strftime("%Y-%m-%d")
    return formatted_date


def format_datetime(datetime_string):
    datetime_obj = datetime.strptime(datetime_string, "%Y/%m/%d %H:%M:%S")
    formatted_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S+00:00")
    return formatted_datetime


def seed_sets():
    sets_data = getSet.all()
    for data in sets_data:
        set_obj = Set(
            id=data.id,
            name=data.name if hasattr(data, "name") else "",
            series=data.series if hasattr(data, "series") else "",
            printed_total=data.printedTotal if hasattr(data, "printedTotal") else 0,
            total=data.total if hasattr(data, "total") else 0,
            unlimited_legality=data.legalities.unlimited
            if hasattr(data.legalities, "unlimited")
            else "",
            standard_legality=data.legalities.standard
            if hasattr(data.legalities, "standard")
            else "",
            expanded_legality=data.legalities.expanded
            if hasattr(data.legalities, "expanded")
            else "",
            ptcgo_code=data.ptcgoCode if hasattr(data, "ptcgoCode") else "",
            release_date=format_date(data.releaseDate)
            if hasattr(data, "releaseDate")
            else "1900-01-01",
            updated_at=format_datetime(data.updatedAt)
            if hasattr(data, "updatedAt")
            else "1900-01-01 00:00:00+00:00",
            symbol=data.images.symbol if hasattr(data.images, "symbol") else "",
            logo=data.images.logo if hasattr(data.images, "logo") else "",
        )
        set_obj.save()


def seed_cards():
    cards_data = getCard.all()
    # cards_data = getCard.where(page=1, pageSize=25)
    # Iterate over the cards and create corresponding model instances
    for card in cards_data:
        set_id = card.set.id
        set_obj = Set.objects.get(id=set_id)
        card_obj = Card(
            id=card.id,
            card_set=set_obj,
        )
        card_obj.save()

        if card.name:
            card_obj.name = card.name

        if card.supertype:
            card_obj.supertype = card.supertype

        if card.subtypes:
            card_obj.subtypes = card.subtypes[0]

        if card.number:
            card_obj.number = card.number

        if card.artist:
            card_obj.artist = card.artist

        if card.rarity:
            card_obj.rarity = card.rarity

        if card.images.small:
            card_obj.small_image = card.images.small

        if card.images.large:
            card_obj.large_image = card.images.large

        try:
            card_obj.tcgplayer_prices_normal = card.tcgplayer.prices.normal.market
        except AttributeError:
            card_obj.tcgplayer_prices_normal = 0.00

        try:
            card_obj.tcgplayer_prices_holo = card.tcgplayer.prices.holofoil.market
        except AttributeError:
            card_obj.tcgplayer_prices_holo = 0.00

        card_obj.save()


def clear_data():
    Card.objects.all().delete()
    # Set.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        # seed_sets()
        seed_cards()
        print("seeded successfully")
