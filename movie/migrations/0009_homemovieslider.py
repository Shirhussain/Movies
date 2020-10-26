# Generated by Django 3.1 on 2020-10-25 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeMovieSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='HomeMovieSlider')),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
    ]