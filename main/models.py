from django.db import models
from django.contrib.auth.models import User


CARD_TYPE_CHOICES = [
    ('colorless', 'Colorless'),
    ('darkness', 'Darkness'),
    ('dragon', 'Dragon'),
    ('fairy', 'Fairy'),
    ('fighting', 'Fighting'),
    ('fire', 'Fire'),
    ('grass', 'Grass'),
    ('lightning', 'Lightning'),
    ('metal', 'Metal'),
    ('psychic', 'Psychic'),
    ('water', 'Water'),
]


# One to One, Each pokemon card has one ability
class Abilities(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    ability_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.text}'


# One to One, Each pokemon card has one ancient trait
class AncientTrait(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

# One to Many, Each pokemon card can have multiple attacks


class Attacks(models.Model):
    cost = models.JSONField(default=list, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    damage = models.CharField(max_length=100, null=True, blank=True)
    converted_energy_cost = models.IntegerField(
        default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


# One to One, Each pokemon card has a unique price
class CardMarket(models.Model):
    url = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)
    prices = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.url}'


# One to One, Each pokemon card has a unique picture
class CardImages(models.Model):
    small_img = models.CharField(max_length=100, null=True, blank=True)
    large_img = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.small_img}'


# One to One, Each pokemon card set has a unique picture
class SetImages(models.Model):
    symbol = models.CharField(max_length=100, null=True, blank=True)
    logo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.logo}'


# Many to Many, Many pokemon cards share many legalities
class Legalities(models.Model):
    LEGALITY_CHOICES = [
        ('legal', 'Legal'),
        ('banned', 'Banned'),
    ]

    standard = models.CharField(
        max_length=100, choices=LEGALITY_CHOICES, default='legal', null=True, blank=True)
    expanded = models.CharField(
        max_length=100, choices=LEGALITY_CHOICES, default='legal', null=True, blank=True)
    unlimited = models.CharField(
        max_length=100, choices=LEGALITY_CHOICES, default='legal', null=True, blank=True)

    def __str__(self):
        return f'Standard: {self.standard} | Expanded: {self.expanded} | Unlimited: {self.unlimited}'


# Many to Many, Many pokemon cards share many resistances
class Resistances(models.Model):
    card_type = models.CharField(
        max_length=100, choices=CARD_TYPE_CHOICES,  null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.card_type}'


# One to Many, Each pokemon card belongs to one set but each set has multiple cards
class CardSet(models.Model):
    card_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    series = models.CharField(max_length=100, null=True, blank=True)
    printed_total = models.IntegerField(
        default=0, null=True, blank=True)
    total = models.IntegerField(
        default=0, null=True, blank=True)
    legalities = models.ManyToManyField(
        Legalities, blank=True, related_name='cardsets_legalities')
    ptcgo_code = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)
    images = models.ManyToManyField(
        SetImages, blank=True, related_name='cardsets_set_images')

    def __str__(self):
        return f'{self.name} - Released: {self.release_date}'


# One to One, Each pokemon card has a unique price
class Tcgplayer(models.Model):
    url = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)
    normal_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    holo_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Price: {self.normal_price} | Holo Price: {self.holo_price}'


# Many to Many, Many pokemon cards share many weaknesses
class Weaknesses(models.Model):
    card_type = models.CharField(
        max_length=100, choices=CARD_TYPE_CHOICES, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.card_type}'


# Card Object based on Pokemon tcg api json data
class Card(models.Model):
    SUPERTYPE_CHOICES = [
        ('pokémon', 'Pokémon'),
        ('trainer', 'Trainer'),
        ('energy', 'Energy'),
    ]
    abilities = models.OneToOneField(
        Abilities, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100, null=True, blank=True)
    ancient_trait = models.OneToOneField(
        AncientTrait, on_delete=models.CASCADE)
    attacks = models.ForeignKey(
        Attacks, null=True, blank=True, on_delete=models.SET_NULL)
    cardmarket = models.OneToOneField(
        CardMarket, on_delete=models.CASCADE)
    converted_retreat_cost = models.IntegerField(
        default=0, null=True, blank=True)
    evolves_from = models.CharField(max_length=100, null=True, blank=True)
    evolves_to = models.JSONField(default=list, null=True, blank=True)
    flavor_text = models.CharField(max_length=100, null=True, blank=True)
    hp = models.CharField(max_length=100, null=True, blank=True)
    card_id = models.CharField(max_length=100, null=True, blank=True)
    images = models.OneToOneField(
        CardImages, on_delete=models.CASCADE)
    legalities = models.ManyToManyField(
        Legalities, blank=True, related_name='cards_legalities')
    level = models.CharField(max_length=100, null=True, blank=True)
    regulation_mark = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    national_pokedex_numbers = models.JSONField(
        default=list, null=True, blank=True)
    number = models.CharField(max_length=3, null=True, blank=True)
    rarity = models.CharField(max_length=100, null=True, blank=True)
    resistances = models.ManyToManyField(
        Resistances, blank=True, related_name='cards_resistances')
    retreat_cost = models.JSONField(default=list, null=True, blank=True)
    rules = models.JSONField(default=list, null=True, blank=True)
    card_set = models.ForeignKey(
        CardSet, null=True, blank=True, on_delete=models.CASCADE)
    subtypes = models.JSONField(default=list, null=True, blank=True)
    supertype = models.CharField(
        max_length=100, choices=SUPERTYPE_CHOICES, null=True, blank=True)
    tcgplayer = models.OneToOneField(
        Tcgplayer, on_delete=models.CASCADE)
    types = models.JSONField(default=list, null=True, blank=True)
    weaknesses = models.ManyToManyField(
        Weaknesses, blank=True, related_name='cards_weaknesses')

    in_collection = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


# Many to Many, each collection can have multiple cards and each card can be in multiple collections
class Collection(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    cards = models.ManyToManyField(Card)

    created_by = models.ForeignKey(
        User, related_name='collection', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
