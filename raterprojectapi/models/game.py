from django.db import models
from .rater import Rater 


class Game(models.Model):

    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    designer = models.CharField(max_length=50)
    year = models.IntegerField()
    player_count = models.IntegerField()
    duration = models.IntegerField()
    age = models.IntegerField()
    
