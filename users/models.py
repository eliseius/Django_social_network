from django import forms
from django.db import models
from django.contrib.auth.models import User


class UserAuthorizationForm(forms.ModelForm):
    username = forms.CharField(min_length=4)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=4)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    confirmpassword = forms.CharField(max_length=40, min_length=8, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def clean_confirmpassword(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirmpassword']:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data['confirmpassword']