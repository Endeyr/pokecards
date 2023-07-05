from pokemontcgsdk import Card as getCard, RestClient
from django.core.management.base import BaseCommand
from ...models import *
from my_secrets import secrets

API_KEY = secrets.API_KEY

RestClient.configure(API_KEY)


def seed_cards():
    # cards = getCard.all()
    cards = getCard.where(page=1, pageSize=2)
    for i in cards:
        # Create instance of Card
        card = Card()

        # Assign attribute values based on api data to CharFields
        try:
            card.artist = i.artist
        except AttributeError:
            card.artist = ""

        try:
            card.converted_retreat_cost = i.convertedRetreatCost
        except AttributeError:
            card.converted_retreat_cost = 0

        try:
            card.evolves_from = i.evolvesFrom
        except AttributeError:
            card.evolves_from = ""

        try:
            card.flavor_text = i.flavorText
        except AttributeError:
            card.flavor_text = ""

        try:
            card.hp = i.hp
        except AttributeError:
            card.hp = ""

        try:
            card.card_id = i.id
        except AttributeError:
            card.card_id = ""

        try:
            card.level = i.level
        except AttributeError:
            card.level = ""

        try:
            card.regulation_mark = i.regulationMark
        except AttributeError:
            card.regulation_mark = ""

        try:
            card.name = i.name
        except AttributeError:
            card.name = ""

        try:
            card.number = i.number
        except AttributeError:
            card.number = ""

        try:
            card.rarity = i.rarity
        except AttributeError:
            card.rarity = ""

        try:
            card.supertype = i.supertype
        except AttributeError:
            card.supertype = ""

        card.save()

        # Handle ManytoManyField
        abilities_data = i.abilities
        if abilities_data is not None:
            for data in abilities_data:
                ability, _ = Abilities.objects.get_or_create(
                    name=data.get("name", ""),
                    text=data.get("text", ""),
                    type=data.get("type", ""),
                )
                card.save()
                card.abilities.add(ability)

        ancient_trait_data = i.ancientTrait
        if ancient_trait_data is not None:
            for data in ancient_trait_data:
                trait, _ = AncientTrait.objects.get_or_create(
                    name=data.get("name", ""),
                    text=data.get("text", ""),
                )
                card.save()
                card.ancient_trait.add(trait)

        attacks_data = i.attacks
        if attacks_data is not None:
            for data in attacks_data:
                attack, _ = Attacks.objects.get_or_create(
                    cost=data.cost if hasattr(data, "cost") else [],
                    name=data.name if hasattr(data, "name") else "",
                    text=data.text if hasattr(data, "text") else "",
                    damage=data.damage if hasattr(data, "damage") else "",
                    converted_energy_cost=data.convertedEnergyCost if hasattr(
                        data, "convertedEnergyCost") else 0,
                )
                card.save()
                card.attacks.add(attack)

        cardmarket_data = i.cardmarket
        if cardmarket_data is not None:
            cm, _ = CardMarket.objects.get_or_create(
                url=cardmarket_data.url if hasattr(
                    cardmarket_data, "url") else "",
                updated_at=cardmarket_data.updated_at if hasattr(
                    cardmarket_data, "updated_at") else "",
                prices=cardmarket_data.prices.averageSellPrice if hasattr(
                    cardmarket_data, "prices.averageSellPrice") else 0,
            )
            card.save()
            card.cardmarket.add(cm)

        images_data = i.images
        if images_data is not None:
            image, _ = Images.objects.get_or_create(
                small_img=images_data.small if hasattr(
                    images_data, "small") else "",
                large_img=images_data.large if hasattr(
                    images_data, "large") else "",
                symbol=images_data.symbol if hasattr(
                    images_data, "symbol") else "",
                logo=images_data.logo if hasattr(images_data, "logo") else "",
            )
            card.save()
            card.images.add(image)

        legalities_data = i.legalities
        if legalities_data is not None:
            legal, _ = Legalities.objects.get_or_create(
                standard=legalities_data.standard if hasattr(
                    legalities_data, "standard") else "",
                expanded=legalities_data.expanded if hasattr(
                    legalities_data, "expanded") else "",
                unlimited=legalities_data.unlimited if hasattr(
                    legalities_data, "unlimited") else "",
            )
            card.save()
            card.legalities.add(legal)

        resistances_data = i.resistances
        if resistances_data is not None:
            resistance, _ = Resistances.objects.get_or_create(
                type=resistances_data.type if hasattr(
                    resistances_data, "type") else "",
                value=resistances_data.value if hasattr(
                    resistances_data, "value") else "",
            )
            card.save()
            card.resistances.add(resistance)

        set_data = i.set
        if set_data is not None:
            cs, _ = CardSet.objects.get_or_create(
                card_id=set_data.id if hasattr(
                    set_data, "id") else "",
                name=set_data.name if hasattr(
                    set_data, "name") else "",
                series=set_data.series if hasattr(
                    set_data, "series") else "",
                printed_total=set_data.printedTotal if hasattr(
                    set_data, "printedTotal") else 0,
                total=set_data.total if hasattr(
                    set_data, "total") else 0,
                ptcgo_code=set_data.ptcgoCode if hasattr(
                    set_data, "ptcgoCode") else "",
                release_date=set_data.releaseDate if hasattr(
                    set_data, "releaseDate") else "",
                updated_at=set_data.updatedAt if hasattr(
                    set_data, "updatedAt") else "",
            )
            img, _ = Images.objects.get_or_create(
                symbol=set_data.images.symbol if hasattr(
                    set_data.images, "symbol") else "",
                logo=set_data.images.logo if hasattr(
                    set_data.images, "logo") else "",
                small_img="",
                large_img="",
            )
            legal, _ = Legalities.objects.get_or_create(
                standard=legalities_data.standard if hasattr(
                    legalities_data, "standard") else "",
                expanded=legalities_data.expanded if hasattr(
                    legalities_data, "expanded") else "",
                unlimited=legalities_data.unlimited if hasattr(
                    legalities_data, "unlimited") else "",
            )
            card.save()
            cs.images.add(img)
            cs.legalities.add(legal)
            card.card_set.add(cs)

        tcgplayer_data = i.tcgplayer
        if tcgplayer_data is not None:
            tcg, _ = Tcgplayer.objects.get_or_create(
                url=tcgplayer_data.url if hasattr(
                    tcgplayer_data, "url") else "",
                updated_at=tcgplayer_data.updatedAt if hasattr(
                    tcgplayer_data, "updatedAt") else "",
                normal_price=tcgplayer_data.prices.TCGPrices if hasattr(
                    tcgplayer_data, "TCGPrices") else 0,
                holo_price=0,
            )
            card.save()
            card.tcgplayer.add(tcg)

        weaknesses_data = i.weaknesses
        if weaknesses_data is not None:
            weak, _ = Weaknesses.objects.get_or_create(
                type=weaknesses_data.type if hasattr(
                    weaknesses_data, "type") else "",
                value=weaknesses_data.value if hasattr(
                    weaknesses_data, "value") else "",
            )
            card.save()
            card.weaknesses.add(weak)

        # Handle JSONField
        # evolves_to
        # national_pokedex_numbers
        # retreat_cost
        # rules
        # subtypes
        # types

        card.save()


def clear_data():
    Card.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        seed_cards()
        print("seeded successfully")
