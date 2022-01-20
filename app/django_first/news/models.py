from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=80)
    rating = models.IntegerField()
    year = models.CharField(max_length=4, null=True)
