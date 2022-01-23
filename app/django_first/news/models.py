from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=80)
    rating = models.IntegerField()
    year = models.CharField(max_length=4, null=True)


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, upload_to='photo/%Y/%m')
    is_publish = models.BooleanField(default=True)
