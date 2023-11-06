from django.contrib.auth.models import User
from django.http import HttpRequest
from django.db.models.query import QuerySet

from datetime import date

from profiles.models import Profile


def update_profile(data: dict[str,str], profile: QuerySet[Profile]) -> str:
    profile.name = data['name']
    profile.surname = data['surname']
    profile.hobbies = data['hobbies']
    profile.gender = data['gender']
    if data.get('birthday') is not None:
        profile.birthday = data['birthday']
    if data.get('avatar') is not None:
        profile.avatar = data['avatar']
    profile.save()
    return 'Профиль обновлен'

    
def create_new_profile(data: dict[str,str], username: str) -> str:
    new_profile = Profile.objects.create(
        name=data['name'],
        surname=data['surname'],
        birthday=data.get('birthday'),
        avatar=data.get('avatar'),
        hobbies=data['hobbies'],
        gender=data['gender'],
        user=User.objects.filter(username=username).first()
    )
    return 'Профиль создан'


def get_profile_user(request: HttpRequest) -> QuerySet[Profile]:
    profile = Profile.objects.filter(user__username=request.user.username).first()
    return profile


def get_initail_form_values(profile) -> dict[str,(str|date)] | None:
    initail_values = {
        'name': profile.name,
        'surname': profile.surname,
        'birthday': profile.birthday,
        'hobbies': profile.hobbies,
        'gender': profile.gender,
    }
    return initail_values
