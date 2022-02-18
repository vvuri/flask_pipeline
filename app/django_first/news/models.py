from django.db import models
from django.urls import reverse


class Movies(models.Model):
    name = models.CharField(max_length=80)
    rating = models.IntegerField()
    year = models.CharField(max_length=4, null=True)


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=False)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    photo = models.ImageField(blank=True, upload_to='photo/%Y/%m')
    is_publish = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')  # add _id

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):  # in fields show as title, default as id
        return self.title

    class Meta:  # Admin interface
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']


class Category(models.Model):
    title = models.CharField(max_length=160, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('news-category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категрия'
        verbose_name_plural = 'Категории'
        ordering = ['title']
