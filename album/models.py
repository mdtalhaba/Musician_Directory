from django.db import models
from musician.models import Musician

class Album(models.Model) :
    albumName = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    albumReleaseDate = models.DateTimeField(auto_now_add=True)
    CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = models.CharField(max_length=5, choices=CHOICES)

    def __str__(self) :
        return self.albumName


