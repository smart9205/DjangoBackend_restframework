# Generated by Django 4.1.6 on 2023-02-10 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0002_alter_movie_genre_ids'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_id',
            new_name='movieID',
        ),
    ]
