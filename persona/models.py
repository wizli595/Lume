from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from pulse.models import Follow

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    @property
    def followers(self):
        return self.followers_set.all()

    @property
    def following(self):
        return self.following_set.all()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"

