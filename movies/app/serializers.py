from rest_framework import serializers

from .models import Comment, Movie


class FetchMovieSerializer(serializers.Serializer):
    """
    validate fetch movie request parameters.
    """

    movie_title = serializers.CharField(max_length=100, required=True)


class MovieSerializer(serializers.ModelSerializer):
    """
    Movie model main serializer
    """

    class Meta:
        model = Movie
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        # to prevent duplication.
        movie, created = Comment.objects.get_or_create(**validated_data)
        return movie
