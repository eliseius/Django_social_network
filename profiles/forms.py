from django import forms

from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    name = forms.CharField(min_length=2)
    surname = forms.CharField(min_length=2)

    class Meta:
        model = Profile
        fields = ('name', 'surname', 'birthday', 'avatar', 'hobbies', 'gender')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
