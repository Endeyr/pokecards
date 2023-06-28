from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


INPUT_CLASSES = "min-w-full text-sm font-medium text-gray-900"


class UserForm(UserCreationForm):
    '''
    Form that uses built-in UserCreationForm to handle user creation
    '''
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'placeholder': '*Your first name...', 'class': INPUT_CLASSES}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'placeholder': '*Your last name...', 'class': INPUT_CLASSES}))
    username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(
        attrs={'placeholder': '*Email...', 'class': INPUT_CLASSES}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': '*Password...', 'class': INPUT_CLASSES}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': '*Confirm Password...', 'class': INPUT_CLASSES}))

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2')
