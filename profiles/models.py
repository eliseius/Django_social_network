from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField()
    avatar = models.ImageField(upload_to='images/')
    hobbies = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=[('m', 'men'), ('w', 'women'), ('o', 'other')])
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return f'Full name {self.name} {self.surname}'
    