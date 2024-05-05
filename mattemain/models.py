from django.db import models


# Create your models here.
class NumberModel(models.Model):
    number_one = models.IntegerField()
    number_two = models.IntegerField()
    summa = models.IntegerField()
    svarat = models.BooleanField(default=False)
    correct = models.BooleanField(default=False)
