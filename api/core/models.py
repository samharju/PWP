from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    """Override default user model"""
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
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)


class Rule(models.Model):
    """Rule model to define size and end condition for game"""
    name = models.CharField(max_length=50, primary_key=True)
    rows = models.PositiveIntegerField(
        default=3,
        validators=[
            MinValueValidator(3, "Min count 3"),
            MaxValueValidator(10, "Max count 10")
        ]
    )
    columns = models.PositiveIntegerField(
        default=3,
        validators=[
            MinValueValidator(3, "Min count 3"),
            MaxValueValidator(10, "Max count 10")
        ]

    )
    winning_tick_count = models.PositiveIntegerField(
        default=3, validators=[
            MinValueValidator(3, "Min count 3"),
            MaxValueValidator(10, "Max count 10")
        ]
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    def save(self, *args, **kwargs):
        """Call full_clean to enforce validation."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """String representation mainly for development and admin site."""
        return str(self.name)


class Game(models.Model):
    """Game model to define a match."""
    player1 = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='starter',
        null=True
    )
    player2 = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='challenger',
        null=True,
        blank=True
    )
    board = models.CharField(blank=True, max_length=100)
    turn = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(3)]
    )
    winner = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(3)]
    )
    rule = models.ForeignKey(Rule, on_delete=models.PROTECT)

    def clean(self, *args, **kwargs):
        """Custom validation"""
        if self.player1 == self.player2:
            raise ValidationError("You can't play against yourself!")

    def save(self, *args, **kwargs):
        """Call full_clean to enforce validation."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """String representation mainly for development and admin site."""
        return f"{self.pk}: {self.player1} vs {self.player2}"
