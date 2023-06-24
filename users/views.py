from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .forms import (
    UserForm,
    AuthForm,
)


class AccountView(View):
    '''
    Class View to display user account page
    '''

    def get(self, request):
        context = {}
        return render(request, "users/account.html", context)


def profile_view(request):
    '''
    View to allow users to update their profile
    '''
    context = {}
    return render(request, 'users/profile.html', context)


class SignUpView(View):
    '''
    Class View for user Sign-up
    '''

    def get(self, request):
        context = {}
        return render(request, "users/sign_up.html", context)

    def post(self, request):
        context = {}
        return redirect(reverse('users:account'))


class SignInView(View):
    '''
    Class View for user Sign-in
    '''

    def get(self, request):
        context = {}
        return render(request, "users/sign_in.html", context)

    def post(self, request):
        context = {}
        return redirect(reverse('users:account'))


def sign_out(request):
    '''
    Basic view to sign out user
    '''
    logout(request)
    return redirect(reverse('users:sign-in'))
