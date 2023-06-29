from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    num = models.CharField(max_length=3, null=True, blank=True)
    set = models.CharField(max_length=256, null=True, blank=True)

    is_holo = models.BooleanField(default=False)
    in_collection = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


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
