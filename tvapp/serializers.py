from rest_framework import serializers

from .models import Movie


class SearchMovieSerialize(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movieID', 'backdrop_path', 'original_title', 'original_language', 'genre_ids', 'popularity', 'overview',
                  'poster_path', 'title', 'release_date', 'video', 'vote_average', 'vote_count')
