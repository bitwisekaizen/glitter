from django.db import models

# Create your models here.
class Gleet(models.Model):
    message = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True,auto_now_add=True)