# Generated by Django 3.1 on 2020-10-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20201025_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
