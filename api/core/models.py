from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        primary_key = True
    win_percentage = models.DecimalField()
    wins = models.IntegerField(),
    losses = models.IntegerField()

class Rules(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    rows = models.IntegerField()
    columns = models.IntegerField()
    winning_tick_count = models.IntegerField()

class Game(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE)
    player2 = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(max_length=100)
    turn = models.IntegerField(MaxValueValidator(3,"Max 2 player"))
    winner = models.IntegerField(MaxValueValidator(3,"Max 2 player"))
    rules = models.ForeignKey(Rules, on_delete=models.PROTECT, minvaluerror(3,"Max 2 player"))

class SoloGame(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(max_length=500)
    turn = models.IntegerField()
    winner = models.IntegerField()
    rules = models.ForeignKey(Rules, on_delete=models.PROTECT)

