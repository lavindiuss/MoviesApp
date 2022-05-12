import requests
from decouple import config
from django.db import transaction

from .models import Movie


class MovieService:
    apikey = config("OMDB_API_KEY")
    api_url = config("OMDB_API_URL")

    def stringify_response(self, response):
        """
        make sure that response values stringified
        """
        _obj = {str(key): str(value) for key, value in response.items()}
        return _obj

    def fetch(self, **kwargs):
        """
        This function will take movie kwargs ie: title
        and do api fetch to get movie data
        """
        movie_title = kwargs.get("movie")
        url = f"{self.api_url}?apikey={self.apikey}&t={movie_title}"
        try:
            response = requests.request("GET", url).json()
            success = response.get("Response", "False") == "True"
            return success, self.stringify_response(
                response
            ) if success else response.get("Error")
        except Exception as e:
            # in case of networking or api connection issues return error but not error 500
            return False, f"ERROR: {e}"

    def get_movie(self, movie_title: str):
        success, fetched_data = self.fetch(movie=movie_title)
        if success:
            # save movie to database and return response
            movie, created = Movie.objects.get_or_create(**fetched_data)
        return success, fetched_data
