from django.db import models
from .user import User


class ContactForm(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_type = models.CharField(choices=(
        ('business', 'business'), ('hr', 'hr'), ('basic', 'basic')), max_length=20, primary_key=True)
    url = models.URLField(blank=True)
