from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from profiles.forms import ProfileForm
from profiles.function import create_new_profile, update_profile
from profiles.models import Profile


def show_profile_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        email_user = request.user.email
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                user_data = form.cleaned_data
                profile = Profile.objects.filter(user__email=email_user).first()
                if profile is None:
                    create_new_profile(user_data,email_user)
                    message = 'Профиль создан'
                else:
                    update_profile(user_data, profile)
                    message = 'Профиль обновлен'
                return HttpResponse(message)
        else:
            form = ProfileForm()
    else:
        return redirect('http://127.0.0.1:8000/sign_in/')
    
    return render(request, 'registration.html', {"form": form,})
