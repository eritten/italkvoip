from django.db import models

# Create your models here.

class Server(models.Model):
    url = models.URLField(max_length=200)
