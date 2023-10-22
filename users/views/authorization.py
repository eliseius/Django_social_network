from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from users.models import UserAuthorizationForm


@csrf_exempt
def process_authorization_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        user_form = UserAuthorizationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            check_user = authenticate(request, username=user.username, password=user.password)
            if check_user is not None:
                login(request, check_user)
                return redirect('/profile/')
        
    message = "Юзернэйм или пароль неверные."
    return render(request, 'authorization.html', context={'message': message})


def authorization_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'authorization.html')
