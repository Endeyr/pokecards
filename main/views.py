from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .forms import (
    CollectionForm,
)
from .models import *


def index(request):
    context = {}
    return render(request, 'main/index.html', context)


def card(request, pk):
    card = Card.objects.get(id=pk)
    attacks = card.attacks
    attacks_list = attacks[1:-1].split("Attack(")[1:]
    attack_details = []
    for attack in attacks_list:
        name_start = attack.find("name='") + len("name='")
        name_end = attack.find("'", name_start)
        name = attack[name_start:name_end]

        cost_start = attack.find("cost=[") + len("cost=[")
        cost_end = attack.find("]", cost_start)
        cost = attack[cost_start:cost_end]

        converted_energy_cost_start = attack.find(
            "convertedEnergyCost=") + len("convertedEnergyCost=")
        converted_energy_cost_end = attack.find(
            ",", converted_energy_cost_start)
        converted_energy_cost = attack[converted_energy_cost_start:converted_energy_cost_end]

        damage_start = attack.find("damage='") + len("damage=")
        damage_end = attack.find("'", damage_start)
        damage = attack[damage_start:damage_end]

        text_start = attack.find("text='") + len("text='")
        text_end = attack.find("'", text_start)
        text_start_alt = attack.find('text="') + len('text="')
        text_end_alt = attack.find('"', text_start_alt)
        if text_start < text_end:
            text = attack[text_start:text_end]
        else:
            text = attack[text_start_alt:text_end_alt]

        attack_details.append({
            "name": name,
            "cost": cost,
            "convertedEnergyCost": converted_energy_cost,
            "damage": damage,
            "text": text
        })

    abilities = card.abilities
    abilities_details = []
    if abilities is not None:
        abilities_list = abilities[1:-1].split("Ability(")[1:]
        for ability in abilities_list:
            name_start = ability.find("name='") + len("name='")
            name_end = ability.find("'", name_start)
            name = ability[name_start:name_end]

            text_start = ability.find("text='") + len("text='")
            text_end = ability.find("'", text_start)
            text_start_alt = ability.find('text="') + len('text="')
            text_end_alt = ability.find('"', text_start_alt)
            if text_start < text_end:
                text = ability[text_start:text_end]
            else:
                text = ability[text_start_alt:text_end_alt]

            type_start = ability.find("type='") + len("type='")
            type_end = ability.find("'", type_start)
            ability_type = ability[type_start:type_end]

            abilities_details.append({
                "name": name,
                "text": text,
                "type": ability_type,
            })

    prices = card.tcgplayer_prices
    price_details = []

    price_list = prices.split("TCGPrices(")[1:]
    for price in price_list:
        market_start = price.find("market=") + len("market=")
        market_end = price.find(",", market_start)
        market = price[market_start:market_end]

        price_details.append({
            "market": market,
        })

    weaknesses = card.weaknesses
    weaknesses_str = weaknesses[1:-1]
    type_start = weaknesses_str.find("type='") + len("type='")
    type_end = weaknesses_str.find("'", type_start)
    weak_type = weaknesses_str[type_start:type_end]

    value_start = weaknesses_str.find("value='") + len("value='")
    value_end = weaknesses_str.find("'", value_start)
    weak_value = weaknesses_str[value_start:value_end]

    weaknesses_details = f"{weak_type}: {weak_value}"

    resistances = card.resistances
    resistances_str = resistances[1:-1]
    type_start = resistances_str.find("type='") + len("type='")
    type_end = resistances_str.find("'", type_start)
    res_type = resistances_str[type_start:type_end]

    value_start = resistances_str.find("value='") + len("value='")
    value_end = resistances_str.find("'", value_start)
    res_value = resistances_str[value_start:value_end]

    resistances_details = f"{res_type}: {res_value}"

    retreat_cost = ', '.join(card.retreat_cost)
    subtypes = ', '.join(card.subtypes)
    types = ', '.join(card.types)

    context = {"card": card, "attack_details": attack_details,
               "price_details": price_details, "weaknesses": weaknesses_details, "resistances": resistances_details, "retreat_cost": retreat_cost, "subtypes": subtypes, "types": types, "abilities": abilities_details}
    return render(request, 'main/card.html', context)


@login_required
def collection(request):
    context = {}
    return render(request, 'main/collection.html', context)


class CreateCollectionView(LoginRequiredMixin, View):
    template_name = 'main/create_collection.html'

    def get(self, request):
        form = CollectionForm()
        message = ''
        context = {'form': form, 'message': message}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CollectionForm()
        message = ''
        context = {'form': form, 'message': message}
        return render(request, self.template_name, context)


class AdvSearchView(View):
    template_name = 'main/adv_search.html'

    def get(self, request):
        message = ''
        context = {'message': message}
        return render(request, self.template_name, context)

    def post(self, request):
        message = ''
        context = {'message': message}
        return render(request, self.template_name, context)


def search_results(request):
    template_name = 'main/search_results.html'
    context = {}
    return render(request, template_name, context)
