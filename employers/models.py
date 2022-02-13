from django.conf import settings
from django.db import models


class Task(models.Model):
    AKTYWNE = 'aktywne'
    ZAKONCZONE = 'zakończone'
    CHOICES = [
        (AKTYWNE, 'aktywne'),
        (ZAKONCZONE, 'zakończone'),
    ]
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valid_until = models.DateTimeField()
    is_published = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='author')
    applicants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='winner', null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
