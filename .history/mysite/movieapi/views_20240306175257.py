from django.shortcuts import render
from rest_framework import generics
from myapp.models import Movie

# Create your views here.
class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = M