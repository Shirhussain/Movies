# Generated by Django 3.1 on 2020-10-25 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
