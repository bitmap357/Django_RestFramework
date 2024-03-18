from myapp.models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.
    class Meta:
        model = Movie
        fields = ('name', 'description', 'rating')