from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from users.forms import UserAuthorizationForm


def authorization_view(request: HttpRequest) ->HttpResponse:
    if request.method == 'POST':
        form = UserAuthorizationForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('/profile/')
        message = 'Не правильный логин или пароль'
    else:
        form = UserAuthorizationForm()
        message = ''
        
    return render(request, 'authorization.html', {"form": form, "message": message})
