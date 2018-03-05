from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Card


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description', 'deadline', 'file', 'position']
        widgets = {'deadline': forms.SelectDateWidget, }
