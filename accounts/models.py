from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=15)
    # password = models.CharField(("password"), max_length=15)
    email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=15)
    # last_name = models.CharField(max_length=15)
    nick_name = models.CharField(max_length=15)
    birthday = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
