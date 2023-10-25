from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from users.forms import UserRegistrationForm


def create_new_user(username: str, email: str, password: str):
    user = User.objects.create(username=username, email=email, password=password)


def ragistration_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email_form = form.cleaned_data['email']
            username_form = form.cleaned_data['username']
            check_email = User.objects.filter(email=email_form).exists()
            check_username = User.objects.filter(username=username_form).exists()
            if not check_username and not check_email:
                create_new_user(
                    username=username_form,
                    email=email_form,
                    password=form.cleaned_data['password'],
                )
                return redirect('/profile/')
        message = "Имя пользователя или email уже зарегистрированы"
    else:
        form = UserRegistrationForm()
        message = ''
        
    return render(request, 'registration.html', {"form": form, "message": message})
