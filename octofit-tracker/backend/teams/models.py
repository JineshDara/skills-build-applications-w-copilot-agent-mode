from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Team(models.Model):
    """Model for team management and group fitness activities"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    members = models.ManyToManyField(User, related_name='team_memberships')
    total_calories_burned = models.IntegerField(default=0)
    total_workouts = models.IntegerField(default=0)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
