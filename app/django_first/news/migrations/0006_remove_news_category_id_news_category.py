# Generated by Django 4.0.1 on 2022-02-05 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_category_news_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category_id',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
        ),
    ]
