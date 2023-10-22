from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from users.models import UserRegistrationForm


@csrf_exempt
def process_ragustration_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            check_email = User.objects.filter(email=new_user.email).first()
            check_username = User.objects.filter(username=new_user.username).first()
            if check_username is None and check_email is None:
                new_user.set_password(new_user.password)
                new_user.save()
                return redirect('/profile/')
            else:
                message = "Имя пользователя или email уже зарегистрированы"
        else:
            message = "Форма заполнена не корректно"
        
    return render(request, 'registration.html', context={'message': message})


def registration_view(request:HttpRequest) -> HttpResponse:
    return render(request, 'registration.html')
