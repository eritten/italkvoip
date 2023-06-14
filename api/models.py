from django.db import models
from django.utils import timezone
# Create your models here.

class Server(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=200)
    last_check = models.DateTimeField('last check   ', default=timezone.now    )
    port = models.IntegerField(default=80)
    created_at = models.DateTimeField('date created', default=timezone.now)
    updated_at = models.DateTimeField('date updated', default=timezone.now)
    ip=models.CharField(max_length=200)
    def __str__(self):
        return self.name
