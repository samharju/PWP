from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    pass

class Rules(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField()
    columns = models.IntegerField()
    winning_tick_count = models.IntegerField()

class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE)
    player2 = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(max_length=100)
    turn = models.IntegerField()
    winner = models.IntegerField()
    rules = models.ForeignKey(Rules)


class SoloGame(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(max_length=100)
    turn = models.IntegerField()
    winner = models.IntegerField()
    rules = models.ForeignKey(Rules)

