from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)


class UserProfile(models.Model):
    bio = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)