from django.db import models
from datetime import datetime
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    dt = models.DateTimeField(default=datetime.now, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)
