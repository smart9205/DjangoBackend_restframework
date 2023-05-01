from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse, JsonResponse

from .serializers import SearchMovieSerialize

from .models import Movie
# Create your views here.


class MovieApiView(generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SearchMovieSerialize

    def get(self, request, *args, **kwargs):

        movies = Movie.objects.all()
        json_Movies = SearchMovieSerialize(movies, many=True)
        return Response({'movies': json_Movies.data})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.save()
        return Response({
            "movie": SearchMovieSerialize(movie, context=self.get_serializer_context()).data,

        })

    def delete(request, pk):
        movie = Movie.objects.filter(movieID=pk)
        movie.delete()
        return HttpResponse("success", status=status.HTTP_200_OK)
