# Generated by Django 3.2.15 on 2022-10-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videolar/', verbose_name='Film Videosu'),
        ),
    ]