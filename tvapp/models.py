from django.db import models

from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Movie(models.Model):
    movieID = models.CharField(max_length=12)
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=128, blank=True)
    original_language = models.CharField(max_length=16)
    original_title = models.CharField(max_length=64)
    # genre_ids=ArrayField(models.IntegerField())
    genre_ids = models.CharField(max_length=128, blank=True)
    overview = models.CharField(max_length=1024)
    popularity = models.FloatField(default=0)
    poster_path = models.CharField(max_length=128)
    release_date = models.CharField(
        max_length=32, blank=True, null=True)
    title = models.CharField(max_length=128)
    video = models.BooleanField(default=False)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    # class Genres(models.Modal):
