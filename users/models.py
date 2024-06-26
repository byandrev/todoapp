from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
