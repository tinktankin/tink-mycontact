from django.db import models

from .user import User


class Group(models.Model):
    name = models.CharField(
        max_length=30, default=None)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
