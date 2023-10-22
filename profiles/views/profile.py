from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def show_profile_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'authorization.html')