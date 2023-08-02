from typing import Any
from django import http
from django.http.response import HttpResponseRedirect
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
    card_data = getCard.find(pk)
    attacks = card_data.attacks
    if card_data.tcgplayer.prices.normal:
        price = card_data.tcgplayer.prices.normal.market
    elif card_data.tcgplayer.prices.holofoil:
        price = card_data.tcgplayer.prices.holofoil.market
    else:
        price = 0.00
    weaknesses = card_data.weaknesses
    resistances = card_data.resistances
    retreat_cost = card_data.retreatCost
    subtypes = card_data.subtypes
    hp = card_data.hp
    types = card_data.types
    abilities = card_data.abilities

    context = {
        "card": card,
        "attacks": attacks,
        "price": price,
        "weaknesses": weaknesses,
        "resistances": resistances,
        "retreat_cost": retreat_cost,
        "subtypes": subtypes,
        "types": types,
        "abilities": abilities,
        "hp": hp,
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
        message = ""
        context = {
            "message": message,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        name = request.POST.get("name")
        supertype = request.POST.get("supertype")
        subtypes = request.POST.get("subtypes")
        types = request.POST.get("types")
        hp = request.POST.get("hp")
        weaknesses = request.POST.get("weaknesses")
        resistances = request.POST.get("resistances")
        retreat_cost = request.POST.get("retreat_cost")
        set = request.POST.get("set")
        artist = request.POST.get("artist")
        rarity = request.POST.get("rarity")

        cards = getCard.where(q=f"name:{name}")

        #     supertype:{supertype} subtypes:{subtypes} types:{types} hp:{hp} weaknesses:{weaknesses} resistances:{resistances} retreatCost:{retreat_cost} set:{set} artist:{artist} rarity:{rarity}"
        # )

        message = ""
        context = {"message": message, "cards": cards}
        return render(request, "main/search_results.html", context)
