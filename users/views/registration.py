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
            return HttpResponseRedirect(self.success_url)
