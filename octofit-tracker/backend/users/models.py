from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class UserProfile(AbstractUser):
    """Extended user profile with fitness tracking information"""
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    total_workouts = models.IntegerField(default=0)
    total_calories_burned = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fitness_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        default='beginner'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username
