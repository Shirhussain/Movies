# Generated by Django 3.1 on 2020-10-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20201024_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielink',
            name='link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]