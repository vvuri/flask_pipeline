from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=80)
    rating = models.IntegerField()
