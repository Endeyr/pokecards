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
    subtypes = models.CharField(max_length=100, blank=True, null=True)  # list(string)
    card_set = models.ForeignKey(
        "Set", on_delete=models.CASCADE, related_name="card_set"
    )  # hash
    number = models.CharField(max_length=100, blank=True, null=True)  # string
    artist = models.CharField(max_length=100, blank=True, null=True)  # string
    rarity = models.CharField(max_length=100, blank=True, null=True)  # string
    small_image = models.URLField(blank=True, null=True)  # url
    large_image = models.URLField(blank=True, null=True)  # url
    tcgplayer_prices_normal = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=8
    )  # hash
    tcgplayer_prices_holo = models.DecimalField(
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
