from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View


class AccountView(View):
    def get(self, request):
        context = {}
        return render(request, "users/account.html")
