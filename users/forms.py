from django import forms


class UserAuthorizationForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=25)
    password = forms.CharField(min_length=8,  widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=25)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=40, widget=forms.PasswordInput)
    confirmpassword = forms.CharField(max_length=40, min_length=8, widget=forms.PasswordInput)

    def clean_confirmpassword(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirmpassword']:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data['confirmpassword']
