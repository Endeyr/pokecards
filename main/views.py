from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'main/index.html', context)


def card(request, pk):
    context = {}
    return render(request, 'main/card.html', context)


def collection(request, pk):
    context = {}
    return render(request, 'main/collection.html', context)
