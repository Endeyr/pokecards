from pokemontcgsdk import Card as getCard, RestClient
from django.core.management.base import BaseCommand
from ...models import *
from my_secrets import secrets

API_KEY = secrets.API_KEY

RestClient.configure(API_KEY)


# TODO

# Fix format on some of the db fields
# Fix attack, abilities, ancient trait,

def seed_cards():
    # cards = getCard.all()
    cards = getCard.where(page=1, pageSize=2)
    # Iterate over the cards and create corresponding model instances
    for card in cards:
        card_obj = Card()
        # Create or get Abilities instance
        abilities_data = card.abilities
        try:
            abilities = Abilities.objects.get(
                name=abilities_data.name,
                text=abilities_data.text,
                ability_type=abilities_data.type,
            )
        except AttributeError:
            abilities = Abilities.objects.create(
                name="",
                text="",
                ability_type="",
            )

        # Create or get AncientTrait instance
        ancient_trait_data = card.ancientTrait
        try:
            ancient_trait = AncientTrait.objects.get(
                name=ancient_trait_data.name,
                text=ancient_trait_data.text,
            )
        except AttributeError:
            ancient_trait = AncientTrait.objects.create(
                name="",
                text="",
            )

        # Create or get Attacks instance
        attacks_data = card.attacks
        for data in attacks_data:
            attack, _ = Attacks.objects.get_or_create(
                name=data.name if hasattr(data, "name") else "",
                cost=data.cost if hasattr(data, "cost") else [],
                text=data.text if hasattr(data, "text") else "",
                damage=data.damage if hasattr(data, "damage") else "",
                converted_energy_cost=data.convertedEnergyCost if hasattr(
                    data, "convertedEnergyCost") else 0,
            )
            attack.card = card_obj
            attack.save()

        # Create or get CardMarket instance
        cardmarket_data = card.cardmarket
        cardmarket, _ = CardMarket.objects.get_or_create(
            url=cardmarket_data.url,
            updated_at=cardmarket_data.updatedAt,
            prices=cardmarket_data.prices.averageSellPrice,
        )

        # Create or get CardImages instance
        card_images_data = card.images
        card_images, _ = CardImages.objects.get_or_create(
            small_img=card_images_data.small,
            large_img=card_images_data.large,
        )

        # Create or get Legalities instance
        legalities_data = card.legalities
        legalities, _ = Legalities.objects.get_or_create(
            standard=legalities_data.standard,
            expanded=legalities_data.expanded,
            unlimited=legalities_data.unlimited,
        )

        # Create or get Resistances instances
        resistances_data = card.resistances
        resistance, _ = Resistances.objects.get_or_create(
            card_type=resistances_data.type if hasattr(
                resistances_data, "type") else "",
            value=resistances_data.value if hasattr(
                resistances_data, "value") else "",
        )

        # Create or get Weaknesses instances
        weaknesses_data = card.weaknesses[0]
        weakness, _ = Weaknesses.objects.get_or_create(
            card_type=weaknesses_data.type,
            value=weaknesses_data.value
        )

        # Create or get CardSet instance
        card_set_data = card.set
        try:
            card_set = CardSet.objects.get(card_id=card_set_data.id)
        except CardSet.DoesNotExist:
            card_set = CardSet.objects.create(
                card_id=card_set_data.id,
                name=card_set_data.name,
                series=card_set_data.series,
                printed_total=card_set_data.printedTotal,
                total=card_set_data.total,
                ptcgo_code=card_set_data.ptcgoCode,
                release_date=card_set_data.releaseDate,
                updated_at=card_set_data.updatedAt
            )

        # Create or get Tcgplayer instance
        tcgplayer_data = card.tcgplayer
        tcgplayer, _ = Tcgplayer.objects.get_or_create(
            url=tcgplayer_data.url,
            updated_at=tcgplayer_data.updatedAt,
            normal_price=tcgplayer_data.prices.normal.market if hasattr(
                tcgplayer_data, "TCGPrices") else 0,
            holo_price=tcgplayer_data.prices.reverseHolofoil.market
        )

        # Create or get Card instance
        card_obj, _ = Card.objects.get_or_create(
            abilities=abilities,
            artist=card.artist,
            ancient_trait=ancient_trait,
            evolves_from=card.evolvesFrom,
            evolves_to=card.evolvesTo if hasattr(
                card, "evolvedTo") else [],
            flavor_text=card.flavorText,
            hp=card.hp,
            card_id=card.id,
            images=card_images,
            level=card.level if hasattr(card, "level") else "",
            regulation_mark=card.regulationMark,
            name=card.name,
            national_pokedex_numbers=card.nationalPokedexNumbers,
            number=card.number,
            rarity=card.rarity,
            retreat_cost=card.retreatCost,
            rules=card.rules,
            card_set=card_set,
            subtypes=card.subtypes,
            supertype=card.supertype,
            tcgplayer=tcgplayer,
            cardmarket=cardmarket,
            types=card.types,
            in_collection=False
        )

        # Add ManyToMany relations
        card_obj.legalities.add(legalities)
        card_obj.resistances.add(resistance)
        card_obj.weaknesses.add(weakness)
        card_obj.save()


def clear_data():
    Card.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        seed_cards()
        print("seeded successfully")
