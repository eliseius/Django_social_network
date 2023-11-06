from django.db import models

from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Profile(models.Model):
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)
    hobbies = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=[('m', 'men'), ('w', 'women'), ('o', 'other')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'Full name {self.name} {self.surname}'


