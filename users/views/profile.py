from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def show_profile_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponse('Вы успешно авторизовались')
    else:
        return render(request, 'authorization.html')