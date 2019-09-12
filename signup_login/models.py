from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatars', default='no_name.png')

    def __str__(self):
        return f'{self.user.username} UserProfile'

