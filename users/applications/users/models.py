from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOISES = (
        ("M", "masculine"),
        ("F", "female"),
        ("0", "others"),
    )

    username = models.CharField(max_length=20, unique=True),
    email = models.EmailField(),
    names = models.CharField(max_length=30),
    last_names = models.CharField(max_length=30),
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES, blank=True),

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.names + " " + self.last_names