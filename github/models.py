from django.db import models

# Create your models here.


class Hiren(models.Model):
    access_token = models.CharField(max_length=200)
    authorized = models.BooleanField(default=False)


class Counter(models.Model):
    number = models.BigIntegerField()
    date = models.DateTimeField()
