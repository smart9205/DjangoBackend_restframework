# Generated by Django 4.1.6 on 2023-02-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0006_alter_movie_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
