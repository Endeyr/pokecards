from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import (
    CollectionForm,
)


def index(request):
    context = {}
    return render(request, 'main/index.html', context)


def card(request, pk):
    context = {}
    return render(request, 'main/card.html', context)


def collection(request, pk):
    context = {}
    return render(request, 'main/collection.html', context)


class CreateCollectionView(View):
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
