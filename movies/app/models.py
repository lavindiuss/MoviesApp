from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Movie(TimeStampedModel):
    """
    field names not following pep8 but i did this to run Movie.objects.get_or_create(**fetched_data) directly for now
    """

    Title = models.CharField(max_length=400, blank=True, null=True)
    Year = models.CharField(max_length=400, blank=True, null=True)
    Rated = models.CharField(max_length=400, blank=True, null=True)
    Released = models.CharField(max_length=400, blank=True, null=True)
    Runtime = models.CharField(max_length=400, blank=True, null=True)
    Genre = models.CharField(max_length=400, blank=True, null=True)
    Director = models.CharField(max_length=400, blank=True, null=True)
    Writer = models.CharField(max_length=400, blank=True, null=True)
    Actors = models.CharField(max_length=400, blank=True, null=True)
    Language = models.CharField(max_length=400, blank=True, null=True)
    Country = models.CharField(max_length=400, blank=True, null=True)
    Awards = models.CharField(max_length=400, blank=True, null=True)
    Poster = models.TextField(blank=True, null=True)
    Ratings = models.CharField(max_length=400, blank=True, null=True)
    Metascore = models.CharField(max_length=400, blank=True, null=True)
    imdbRating = models.CharField(max_length=400, blank=True, null=True)
    imdbVotes = models.CharField(max_length=400, blank=True, null=True)
    imdbID = models.CharField(max_length=400, blank=True, null=True)
    Type = models.CharField(max_length=400, blank=True, null=True)
    DVD = models.CharField(max_length=100, blank=True, null=True)
    BoxOffice = models.CharField(max_length=400, blank=True, null=True)
    Production = models.CharField(max_length=400, blank=True, null=True)
    Website = models.CharField(max_length=400, blank=True, null=True)
    Plot = models.TextField(blank=True, null=True)
    Response = models.CharField(max_length=400, blank=True, null=True)
    totalSeasons = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.Title


class Comment(TimeStampedModel):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="comments",
        help_text="Movie relation",
    )
    body = models.TextField()

    def __str__(self):
        if self.movie:
            return f"{self.movie.Title}-Movie comment {self.id}"
        return self.id
