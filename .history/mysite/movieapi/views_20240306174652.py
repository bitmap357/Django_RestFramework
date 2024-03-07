from django.shortcuts import render
from rest_framework import generics
from myapp.models import Movie

# Create your views here.
class MovieAPIView(generics.ListAPIView):
    querysetMovie.objects.all()