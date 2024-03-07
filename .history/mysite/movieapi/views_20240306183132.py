from django.shortcuts import render
from rest_framework import generics
from myapp.models import Movie
from .serializers import MovieSerializer

# Create your views here.
class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieDetail(generics.Re):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer