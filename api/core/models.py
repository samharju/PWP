from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
        primary_key=True
    )
    win_percentage = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=3
    )
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)


class Rules(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    rows = models.IntegerField(
        default=3, validators=[MinValueValidator(3, "Min count 3")]
    )
    columns = models.IntegerField(
        default=3, validators=[MinValueValidator(3, "Min count 3")]
    )
    winning_tick_count = models.IntegerField(
        default=3, validators=[MinValueValidator(3, "Min count 3")]
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Game(models.Model):
    player1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='starter'
    )
    player2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='challenger',
        null=True,
        blank=True,
    )
    board = models.CharField(blank=True, max_length=100)
    turn = models.IntegerField(
        default=0, validators=[MaxValueValidator(3, "Max 2 player")]
    )
    winner = models.IntegerField(
        default=0, validators=[MaxValueValidator(3, "Max 2 player")]
    )
    rules = models.ForeignKey(Rules, on_delete=models.PROTECT)

    def clean(self, *args, **kwargs):
        if self.player1 == self.player2:
            raise ValidationError("You can't play against yourself!")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class SoloGame(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(blank=True, max_length=500)
    turn = models.IntegerField(
        default=0, validators=[MaxValueValidator(3, "Max 2 player")]
    )
    winner = models.IntegerField(
        default=0, validators=[MaxValueValidator(3, "Max 2 player")]
    )
    rules = models.ForeignKey(Rules, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
