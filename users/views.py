from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .forms import (
    UserForm,
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
    Class-based view for user sign-up
    '''
    template_name = 'users/sign_up.html'
    form_class = UserForm()

    def get(self, request):
        form = self.form_class
        message = ''
        context = {"form": form, "message": message}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()
            login(request, user)
            return redirect('users:account')

        message = "Registration failed!"
        context = {"form": form, "message": message}
        return render(request, self.template_name, context)


class SignInView(View):
    '''
    Class-based view for user sign-in
    '''
    template_name = 'users/sign_in.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:account')
        else:
            message = "Invalid username and/or password."
            context = {"message": message}
            return render(request, self.template_name, context)


def sign_out(request):
    '''
    Basic view to sign out user
    '''
    logout(request)
    return redirect(reverse('users:sign-in'))
