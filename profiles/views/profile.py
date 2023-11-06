from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from profiles.forms import ProfileForm
from profiles.function import (create_new_profile, update_profile,
                               get_profile_user, get_initail_form_values)


def show_profile_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        username = request.user.username
        profile = get_profile_user(request)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=False)
                if profile is None:
                    message = create_new_profile(form.cleaned_data, username)
                else:
                    message = update_profile(form.cleaned_data, profile)
                return HttpResponse(message)
        else:
            form = ProfileForm()
            if profile is not None:
                initail_values = get_initail_form_values(profile)
                form = ProfileForm(initail_values)
            return render(request, 'profile.html', {"form": form, "profile": profile}) 
    else:
        return redirect('http://127.0.0.1:8000/sign_in/')
