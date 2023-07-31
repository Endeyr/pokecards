from django.db import models
from django.contrib.auth.models import User


class Set(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # string
    name = models.CharField(max_length=100, blank=True, null=True)  # string
    series = models.CharField(max_length=100, blank=True, null=True)  # string
    # int
    printed_total = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)  # int
    unlimited_legality = models.CharField(
        max_length=100, blank=True, null=True
    )  # string
    standard_legality = models.CharField(
        max_length=100, blank=True, null=True
    )  # string
    expanded_legality = models.CharField(
        max_length=100, blank=True, null=True
    )  # string
    ptcgo_code = models.CharField(max_length=100, blank=True, null=True)  # string
    release_date = models.DateField(blank=True, null=True)  # date
    updated_at = models.DateTimeField(blank=True, null=True)  # datetime
    symbol = models.URLField(blank=True, null=True)  # url
    logo = models.URLField(blank=True, null=True)  # url

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"


class Card(models.Model):
    id = models.CharField(max_length=100, primary_key=True)  # string
    name = models.CharField(max_length=100, blank=True, null=True)  # string
    supertype = models.CharField(max_length=100, blank=True, null=True)  # string
    subtypes = models.JSONField(blank=True, null=True)  # list(string)
    level = models.CharField(max_length=100, blank=True, null=True)  # string
    hp = models.CharField(max_length=100, blank=True, null=True)  # string
    types = models.JSONField(blank=True, null=True)  # list(string)
    evolves_from = models.CharField(max_length=100, blank=True, null=True)  # string
    evolves_to = models.JSONField(blank=True, null=True)  # list(string)
    rules = models.JSONField(blank=True, null=True)  # list(string)
    ancient_trait_name = models.CharField(
        max_length=100, blank=True, null=True
    )  # string
    ancient_trait_text = models.CharField(
        max_length=100, blank=True, null=True
    )  # string
    ability_name = models.CharField(max_length=100, blank=True, null=True)  # list(hash)
    ability_text = models.CharField(max_length=100, blank=True, null=True)  # list(hash)
    ability_type = models.CharField(max_length=100, blank=True, null=True)  # list(hash)
    attack_one = models.JSONField(blank=True, null=True)  # list(hash)
    attack_two = models.JSONField(blank=True, null=True)  # list(hash)
    attack_three = models.JSONField(blank=True, null=True)  # list(hash)
    weaknesses_one = models.JSONField(blank=True, null=True)  # list(hash)
    weaknesses_two = models.JSONField(blank=True, null=True)  # list(hash)
    weaknesses_three = models.JSONField(blank=True, null=True)  # list(hash)
    resistances_one = models.JSONField(blank=True, null=True)  # list(hash)
    resistances_two = models.JSONField(blank=True, null=True)  # list(hash)
    resistances_three = models.JSONField(blank=True, null=True)  # list(hash)
    retreat_cost = models.JSONField(blank=True, null=True)  # list(string)
    converted_retreat_cost = models.IntegerField(null=True, blank=True)  # int
    card_set = models.ForeignKey(
        "Set", on_delete=models.CASCADE, related_name="card_set"
    )  # hash
    number = models.CharField(max_length=100, blank=True, null=True)  # string
    artist = models.CharField(max_length=100, blank=True, null=True)  # string
    rarity = models.CharField(max_length=100, blank=True, null=True)  # string
    flavor_text = models.TextField(blank=True, null=True)  # string
    national_pokedex_numbers = models.JSONField(blank=True, null=True)  # list(integer)
    unlimited_legality = models.CharField(
        max_length=100, blank=True, null=True
    )  # string
    standard_legality = models.CharField(
        max_length=100, blank=True, null=True
    )  # string
    expanded_legality = models.CharField(
        max_length=100, blank=True, null=True
    )  # string
    regulation_mark = models.CharField(max_length=100, blank=True, null=True)  # string
    small_image = models.URLField(blank=True, null=True)  # url
    large_image = models.URLField(blank=True, null=True)  # url
    tcgplayer_url = models.URLField(blank=True, null=True)  # url
    tcgplayer_updated_at = models.DateField(blank=True, null=True)  # date
    tcgplayer_prices_normal = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=8
    )  # hash
    tcgplayer_prices_holo = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=8
    )  # hash
    cardmarket_url = models.URLField(blank=True, null=True)  # url
    cardmarket_updated_at = models.DateField(blank=True, null=True)  # date
    cardmarket_prices_normal = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=8
    )  # hash
    cardmarket_prices_holo = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=8
    )  # hash

    in_collection = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"


class Collection(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    # card id is stored here like a favorites field
    cards = models.ManyToManyField(
        Card, related_name="inCollection", default=None, blank=True
    )

    created_by = models.ForeignKey(
        User, related_name="collection", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
