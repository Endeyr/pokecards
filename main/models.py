from django.db import models
from django.contrib.auth.models import User


SUPERTYPE_CHOICES = [
    ('pokemon', 'Pokemon'),
    ('trainer', 'Trainer'),
    ('energy', 'Energy'),
]

TYPE_CHOICES = [
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

LEGALITY_CHOICES = [
    ('legal', 'Legal'),
    ('banned', 'Banned'),
]


class Abilities(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Ability: {self.name} - {self.text}'


class AncientTrait(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Ancient Trait: {self.name}'


class Attacks(models.Model):
    cost = models.JSONField(default=list, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    damage = models.CharField(max_length=100, null=True, blank=True)
    converted_energy_cost = models.IntegerField(
        default=0, null=True, blank=True)

    def __str__(self):
        return f'Attack: {self.name}'


class CardMarket(models.Model):
    url = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)
    prices = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'URL: {self.url}'


class Images(models.Model):
    small_img = models.CharField(max_length=100, null=True, blank=True)
    large_img = models.CharField(max_length=100, null=True, blank=True)
    symbol = models.CharField(max_length=100, null=True, blank=True)
    logo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Small Image: {self.small_img}'


class Legalities(models.Model):
    standard = models.CharField(
        max_length=100, choices=LEGALITY_CHOICES, default='legal', null=True, blank=True)
    expanded = models.CharField(
        max_length=100, choices=LEGALITY_CHOICES, default='legal', null=True, blank=True)
    unlimited = models.CharField(
        max_length=100, choices=LEGALITY_CHOICES, default='legal', null=True, blank=True)

    def __str__(self):
        return f'Standard: {self.standard} | Expanded: {self.expanded} | Unlimited: {self.unlimited}'


class Resistances(models.Model):
    type = models.CharField(
        max_length=100, choices=TYPE_CHOICES,  null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Resistance: {self.type}'


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
        Images, blank=True, related_name='cardsets_images')

    def __str__(self):
        return f'Set: {self.name} - Release Date: {self.release_date}'


class Tcgplayer(models.Model):
    url = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)
    normal_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    holo_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Price: {self.normal_price} | Holo Price: {self.holo_price}'


class Weaknesses(models.Model):
    type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Weakness: {self.type}'


class Card(models.Model):
    abilities = models.ManyToManyField(
        Abilities, blank=True, related_name='cards_abilities')
    artist = models.CharField(max_length=100, null=True, blank=True)
    ancient_trait = models.ManyToManyField(
        AncientTrait, blank=True, related_name='cards_ancient_trait')
    attacks = models.ManyToManyField(
        Attacks, blank=True, related_name='cards_attacks')
    cardmarket = models.ManyToManyField(
        CardMarket, blank=True, related_name='cards_cardmarket')
    converted_retreat_cost = models.IntegerField(
        default=0, null=True, blank=True)
    evolves_from = models.CharField(max_length=100, null=True, blank=True)
    evolves_to = models.JSONField(default=list, null=True, blank=True)
    flavor_text = models.CharField(max_length=100, null=True, blank=True)
    hp = models.CharField(max_length=100, null=True, blank=True)
    card_id = models.CharField(max_length=100, null=True, blank=True)
    images = models.ManyToManyField(
        Images, blank=True, related_name='cards_images')
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
    card_set = models.ManyToManyField(
        CardSet, blank=True, related_name='cards_card_set')
    subtypes = models.JSONField(default=list, null=True, blank=True)
    supertype = models.CharField(
        max_length=100, choices=SUPERTYPE_CHOICES, null=True, blank=True)
    tcgplayer = models.ManyToManyField(
        Tcgplayer, blank=True, related_name='cards_tcgplayer')
    types = models.JSONField(default=list, null=True, blank=True)
    weaknesses = models.ManyToManyField(
        Weaknesses, blank=True, related_name='cards_weaknesses')

    in_collection = models.BooleanField(default=False)

    def __str__(self):
        return f'Name: {self.name}'


class Collection(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    cards = models.ManyToManyField(Card)

    created_by = models.ForeignKey(
        User, related_name='collection', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Title: {self.title}'
