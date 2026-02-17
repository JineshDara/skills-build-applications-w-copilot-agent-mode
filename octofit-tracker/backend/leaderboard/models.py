from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Leaderboard(models.Model):
    """Model for tracking leaderboard rankings"""
    LEADERBOARD_TYPES = [
        ('calories', 'Calories Burned'),
        ('workouts', 'Total Workouts'),
        ('distance', 'Distance Covered'),
        ('duration', 'Time Exercised'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard')
    rank = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    calories_burned = models.IntegerField(default=0)
    total_workouts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-points', '-calories_burned']

    def __str__(self):
        return f"{self.user.username} - Rank {self.rank}"
