from django.db import models

# Create your models here.
class Movie(models.Model):
    
    def __str__(self):
        return super().__str__()
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    rating = models.FloatField()