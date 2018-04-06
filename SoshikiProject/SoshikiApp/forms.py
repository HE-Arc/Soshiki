from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Card, List, Table, Comment


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CardForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    deadline = forms.SplitDateTimeField(input_time_formats=['%H:%M'], input_date_formats=['%d/%m/%Y'])
    file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget.widgets[0].attrs.update({'class': 'datepicker', 'placeholder': 'Date',
                                                                'style': 'margin-bottom:10px;'})
        self.fields['deadline'].widget.widgets[1].attrs.update({'class': 'clockpicker', 'placeholder': 'Hour'})

    class Meta:
        model = Card
        fields = ['title', 'description', 'deadline', 'file']


class ListForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))

    class Meta:
        model = List
        fields = ['name']


class TableForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    favorite = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Table
        fields = ['name', 'background', 'favorite']


class CommentForm(forms.ModelForm):

    value = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment here...'}))

    class Meta:
        model = Comment
        fields = ['value']


class UserUpdateForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
