from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import filters

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.
from .models import Movie, Comment
from .serializers import FetchMovieSerializer, MovieSerializer, CommentSerializer
from .services import MovieService


class MoviesView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filter_fields = [
        "id",
        "Country",
        "Language",
        "Rated",
        "totalSeasons",
        "Type",
    ]
    ordering_fields = ["id", "Country", "Language", "Type"]
    search_fields = ["Title", "imdbID", "Actors", "Writer"]

    def post(self, request, *args, **kwargs):
        serializer = FetchMovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        success, data = MovieService().get_movie(
            movie_title=request.data.get("movie_title")
        )
        if success:
            return Response({"detail": data}, status=status.HTTP_200_OK)

        else:
            return Response(
                {"non_field_errors": data}, status=status.HTTP_400_BAD_REQUEST
            )


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    filter_fields = [
        "id",
        "movie__id",
        "movie__Title",
    ]
    ordering_fields = ["id", "movie__id"]
