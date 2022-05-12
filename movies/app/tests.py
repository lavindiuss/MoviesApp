from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class MoviesTestCases(APITestCase):
    def test_get_movie(self):
        url = reverse("movies")
        response = self.client.post(url, data={"movie_title": "django"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_movies(self):
        url = reverse("movies")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_for_movie(self):
        url = f"{reverse('movies')}?search=Leonardo DiCaprio"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_results(self):
        url = f"{reverse('movies')}?ordering=-id"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommentTestCases(APITestCase):
    def test_create_comment(self):
        # create a movie
        movies_url = reverse("movies")
        response = self.client.post(movies_url, data={"movie_title": "django"})
        # add a comment for the created movie
        url = reverse("comments")
        movies_response = self.client.get(movies_url)
        movies_response = movies_response.json()
        movie_id = movies_response.get("results")[0]["id"]
        response = self.client.post(url, data={"movie": movie_id, "body": "test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_comments(self):
        url = reverse("comments")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_comments_by_movie_title(self):
        url = f'{reverse("comments")}?movie__Title=Django'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
