from django import forms
from django.contrib.auth.models import User


def check_unique_email(value):
    check_email = User.objects.filter(email=value).exists()
    if check_email:
        raise forms.ValidationError('Email уже зарегистрирован')

        
def check_unique_username(value):
    check_username = User.objects.filter(username=value).exists()
    if check_username:
        raise forms.ValidationError('Логин уже занят')
