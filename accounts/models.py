from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    DEVELOPER = 'developer'
    EMPLOYER = 'employer'
    TYPES = [
        (DEVELOPER, 'developer'),
        (EMPLOYER, 'employer'),
    ]
    email = models.EmailField(unique=True)
    postcode = models.CharField(max_length=6, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=128, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%d/%b/%Y/', null=True, blank=True)
    user_type = models.CharField(max_length=9, choices=TYPES, default=DEVELOPER)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.first_name } {self.last_name}'
