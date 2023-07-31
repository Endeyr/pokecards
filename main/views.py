from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.views.generic.edit import CreateView
from django.db.models.functions import Cast
from django.db.models import IntegerField
from pokemontcgsdk import Card as getCard, RestClient, Set as getSet
from my_secrets import secrets

from .forms import (
    CollectionForm,
)
from .models import *


API_KEY = secrets.API_KEY

RestClient.configure(API_KEY)


def index(request):
    context = {}
    return render(request, "main/index.html", context)


def card(request, pk):
    card = Card.objects.get(id=pk)

    context = {
        "card": card,
        # "attack": attack_details,
        # "price": price_details,
        # "weaknesses": weaknesses_details,
        # "resistances": resistances_details,
        # "retreat_cost": retreat_cost,
        # "subtypes": subtypes,
        # "types": types,
        # "abilities": abilities_details,
    }
    return render(request, "main/card.html", context)


@login_required
def collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    cards = collection.cards.all()
    context = {"collection": collection, "cards": cards}
    return render(request, "main/collection.html", context)


class CreateCollectionView(LoginRequiredMixin, CreateView):
    template_name = "main/create_collection.html"
    model = Collection
    fields = ["title", "description"]

    def get(self, request):
        form = CollectionForm()
        message = ""
        context = {"form": form, "message": message}
        return render(request, self.template_name, context)

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("main:collection", kwargs={"pk": self.object.id})


def is_valid_query(param):
    return param != "" and param is not None


class AdvSearchView(View):
    template_name = "main/adv_search.html"

    def get(self, request):
        cards = Card.objects.all().order_by("name")

        name = request.GET.get("name")
        supertype = request.GET.get("supertype")
        subtypes = request.GET.get("subtypes")
        types = request.GET.get("types")
        hp_min = request.GET.get("hp_min")
        hp_max = request.GET.get("hp_max")
        weaknesses = request.GET.get("weaknesses")
        resistances = request.GET.get("resistances")
        retreat_min = request.GET.get("retreat_min")
        retreat_max = request.GET.get("retreat_max")
        set = request.GET.get("set")
        artist = request.GET.get("artist")
        rarity = request.GET.get("rarity")

        if is_valid_query(name):
            cards = cards.filter(name__icontains=name)

        elif is_valid_query(supertype):
            cards = cards.filter(supertype=supertype)

        # Need to fix model data
        elif subtypes:
            cards = cards.filter(subtypes__icontains=subtypes)

        elif types:
            cards = cards.filter(types__icontains=types)

        elif is_valid_query(weaknesses):
            cards = cards.filter(weaknesses__icontains=weaknesses)

        elif is_valid_query(resistances):
            cards = cards.filter(resistances__icontains=resistances)

        elif is_valid_query(set):
            cards = cards.filter(card_set__icontains=set)

        elif is_valid_query(artist):
            cards = cards.filter(artist__icontains=artist)

        elif is_valid_query(rarity):
            cards = cards.filter(rarity=rarity)

        # Need to convert hp to int
        if is_valid_query(hp_min):
            cards = cards.annotate(
                hp_integer=Cast("hp", output_field=IntegerField())
            ).filter(hp_integer__gte=hp_min)

        if is_valid_query(hp_max):
            cards = cards.annotate(
                hp_integer=Cast("hp", output_field=IntegerField())
            ).filter(hp_integer__lt=hp_max)

        if is_valid_query(retreat_min):
            cards = cards.filter(retreat_cost__gte=retreat_min)

        if is_valid_query(retreat_max):
            print(cards)
            cards = cards.filter(retreat_cost__lt=retreat_max)

        message = ""
        context = {"message": message, "cards": cards}
        return render(request, self.template_name, context)

    def post(self, request):
        message = ""
        context = {"message": message}
        return render(request, self.template_name, context)
