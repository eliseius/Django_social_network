from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from profiles.forms import ProfileForm
from profiles.models import Profile


def show_profile_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid:
                check_email = Profile.objects.filter(email=form.cleaned_data['email']).exists()
                if not check_email:
                    create_new_profile(
                        name=form.cleaned_data['name'],
                        surname=form.cleaned_data['surname'],
                        birthday=form.cleaned_data.get('birthday'),
                        avatar=form.cleaned_data.get('avatar'),
                        hobbies=form.cleaned_data['hobbies'],
                        gender=form.cleaned_data['gender'],
                        email=form.cleaned_data['email']
                    )

                    pass

        else:
            form = ProfileForm()
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('sign_in/')
    

def create_new_profile():
    pass
