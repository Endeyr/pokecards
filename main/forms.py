from django.contrib.auth.models import User
from django import forms
from .models import Card, Collection

INPUT_CLASSES = "min-w-full text-sm font-medium text-gray-900"


class CollectionForm(forms.ModelForm):
    '''
    Basic model-form for users to create a collection
    '''
    title = forms.CharField(max_length=256, required=True, widget=forms.TextInput(
        attrs={'placeholder': '*Title...', 'class': INPUT_CLASSES}))
    description = forms.CharField(max_length=256, required=True, widget=forms.TextInput(
        attrs={'placeholder': '*Description...', 'class': INPUT_CLASSES}))

    class Meta:
        model = Collection
        fields = ('title', 'description')
