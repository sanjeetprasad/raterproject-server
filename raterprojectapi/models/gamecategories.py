from django.db import models
from .rater import Rater
from .game import Game

class GameCategory(models.Model):

    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    