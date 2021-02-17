from django.db import models
from .rater import Rater
from .game import Game

class Rating(models.Model):

    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    rating = models.IntegerField()