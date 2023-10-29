from django.contrib.auth.models import User

from profiles.models import Profile


def update_profile(data:dict[str,str], profile):
        profile.name = data['name']
        profile.surname = data['surname']
        profile.birthday = data.get('birthday')
        profile.avatar = data.get('avatar')
        profile.hobbies = data['hobbies']
        profile.gender = data['gender']
        profile.save()

    
def create_new_profile(data:dict[str,str], email:str):
    new_profile = Profile.objects.create(
        name=data['name'],
        surname=data['surname'],
        birthday=data.get('birthday'),
        avatar=data.get('avatar'),
        hobbies=data['hobbies'],
        gender=data['gender'],
        user=User.objects.filter(email=email).first()
    )
