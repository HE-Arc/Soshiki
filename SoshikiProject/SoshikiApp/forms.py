from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminSplitDateTime
from django.contrib.auth.models import User
from .models import Card, List, Table


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CardForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    deadline = forms.SplitDateTimeField(input_time_formats=['%H:%M'], input_date_formats=['%d/%m/%Y'])
    file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    position = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}))

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget.widgets[0].attrs.update({'class': 'datepicker', 'placeholder': 'Date',
                                                                'style': 'margin-bottom:10px;'})
        self.fields['deadline'].widget.widgets[1].attrs.update({'class': 'clockpicker', 'placeholder': 'Hour'})

    class Meta:
        model = Card
        fields = ['title', 'description', 'deadline', 'file', 'position']


class ListForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    position = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                  'placeholder': '0'}))

    class Meta:
        model = List
        fields = ['name', 'position']


class TableForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    favorite = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    background = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Table
        fields = ['name','background', 'favorite']
