from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView

from users.forms import UserRegistrationForm


def create_new_user(username: str, email: str, password: str):
    user = User.objects.create(username=username, email=email, password=password)


class RegistrationFormView(FormView):
    template_name = "registration.html"
    form_class = UserRegistrationForm
    success_url = "/profile/"

    def form_valid(self, form) -> HttpResponse:
        create_new_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        return HttpResponseRedirect(self.success_url)
