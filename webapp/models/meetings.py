from django.db import models
from .user import User
#from django.dispatch import receiver
#from django.db.models.signals import pre_save

class Meeting(models.Model):
    title=models.CharField(max_length=30, default=None)
    location=models.CharField(max_length=30, default=None)
    notes=models.CharField(max_length=30, default=None)
    attendees=models.CharField(max_length=10)
    date=models.DateTimeField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
