# Generated by Django 4.1.6 on 2023-02-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre_ids',
            field=models.CharField(max_length=128),
        ),
    ]
