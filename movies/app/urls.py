from django.urls import path

from .views import MoviesView, CommentsView

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("comments/", CommentsView.as_view()),
]
