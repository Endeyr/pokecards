from pokemontcgsdk import Card as getCard, RestClient, Set as getSet
from django.core.management.base import BaseCommand
from ...models import *
from my_secrets import secrets
from datetime import datetime
from django.utils import timezone

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
            name=data.name if hasattr(
                data, "name") else "",
            series=data.series if hasattr(
                data, "series") else "",
            printed_total=data.printedTotal if hasattr(
                data, "printedTotal") else 0,
            total=data.total if hasattr(
                data, "total") else 0,
            unlimited_legality=data.legalities.unlimited if hasattr(
                data.legalities, "unlimited") else "",
            standard_legality=data.legalities.standard if hasattr(
                data.legalities, "standard") else "",
            expanded_legality=data.legalities.expanded if hasattr(
                data.legalities, "expanded") else "",
            ptcgo_code=data.ptcgoCode if hasattr(
                data, "ptcgoCode") else "",
            release_date=format_date(data.releaseDate) if hasattr(
                data, "releaseDate") else "1900-01-01",
            updated_at=format_datetime(data.updatedAt) if hasattr(
                data, "updatedAt") else "1900-01-01 00:00:00+00:00",
            symbol=data.images.symbol if hasattr(
                data.images, "symbol") else "",
            logo=data.images.logo if hasattr(
                data.images, "logo") else "",
        )
        set_obj.save()


def seed_cards():
    cards_data = getCard.all()
    # Iterate over the cards and create corresponding model instances
    for card in cards_data:
        set_id = card.set.id
        set_obj = Set.objects.get(id=set_id) if set_id else ""
        card_obj = Card(
            id=card.id,
            name=card.name if hasattr(
                card, "name") else "",
            supertype=card.supertype if hasattr(
                card, "supertype") else "",
            subtypes=card.subtypes if hasattr(
                card, "subtypes") else [],
            hp=card.hp if hasattr(
                card, "hp") else "",
            types=card.types if hasattr(
                card, "types") else [],
            evolves_from=card.evolvesFrom if hasattr(
                card, "evolvesFrom") else "",
            evolves_to=card.evolvesTo if hasattr(card, "evolvesTo") else "",
            rules=card.rules if hasattr(
                card, "rules") else "",
            ancient_trait_name=card.ancientTrait.name if hasattr(
                card.ancientTrait, "name") else "",
            ancient_trait_text=card.ancientTrait.text if hasattr(
                card.ancientTrait, "text") else "",
            abilities=card.abilities if hasattr(
                card, "abilities") else [],
            attacks=card.attacks if hasattr(
                card, "attacks") else [],
            weaknesses=card.weaknesses if hasattr(
                card, "weaknesses") else [],
            resistances=card.resistances if hasattr(
                card, "resistances") else [],
            retreat_cost=card.retreatCost if hasattr(
                card, "retreatCost") else [],
            converted_retreat_cost=card.convertedRetreatCost if hasattr(
                card, "convertedRetreatCost") else 0,
            card_set=set_obj,
            number=card.number if hasattr(
                card, "number") else "",
            artist=card.artist if hasattr(
                card, "artist") else "",
            rarity=card.rarity if hasattr(
                card, "rarity") else "",
            flavor_text=card.flavorText if hasattr(
                card, "flavorText") else "",
            national_pokedex_numbers=card.nationalPokedexNumbers if hasattr(
                card, "nationalPokedexNumber") else "",
            unlimited_legality=card.legalities.unlimited if hasattr(
                card.legalities, "unlimited") else "",
            standard_legality=card.legalities.standard if hasattr(
                card.legalities, "standard") else "",
            expanded_legality=card.legalities.expanded if hasattr(
                card.legalities, "expanded") else "",
            regulation_mark=card.regulationMark if hasattr(
                card, "regulationMark") else "",
            small_image=card.images.small if hasattr(
                card.images, "small") else "",
            large_image=card.images.large if hasattr(
                card.images, "large") else "",
            tcgplayer_url=card.tcgplayer.url if hasattr(
                card.tcgplayer, "url") else "",
            tcgplayer_updated_at=format_date(card.tcgplayer.updatedAt) if hasattr(
                card.tcgplayer, "updated_at") else "1900-01-01",
            tcgplayer_prices=card.tcgplayer.prices if hasattr(
                card.tcgplayer, "prices") else 0,
            cardmarket_url=card.cardmarket.url if hasattr(
                card.cardmarket, "url") else "",
            cardmarket_updated_at=format_date(card.cardmarket.updatedAt) if hasattr(
                card.cardmarket, "updated_at") else "1900-01-01",
            cardmarket_prices=card.cardmarket.prices if hasattr(
                card.cardmarket, "prices") else 0,
        )
        card_obj.save()


def clear_data():
    Card.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        seed_sets()
        seed_cards()
        print("seeded successfully")
