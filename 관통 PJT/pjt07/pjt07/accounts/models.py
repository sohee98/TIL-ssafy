from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    follwings = models.ManyToManyField('self', symmetrical=False, related_name='follwers')

