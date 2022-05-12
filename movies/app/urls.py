from django.urls import path

from .views import CommentsView, MoviesView

urlpatterns = [
    path("movies/", MoviesView.as_view(), name="movies"),
    path("comments/", CommentsView.as_view(), name="comments"),
]
