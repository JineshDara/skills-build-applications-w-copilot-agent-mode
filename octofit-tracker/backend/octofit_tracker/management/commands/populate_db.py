from django.core.management.base import BaseCommand

from users.models import UserProfile
from teams.models import Team
from activities.models import Activity
from leaderboard.models import Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data

        UserProfile.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams

        marvel = Team.objects.create(name='Team Marvel', creator=None)
        dc = Team.objects.create(name='Team DC', creator=None)

        # Create Users (Superheroes)

        users = [
            UserProfile.objects.create_user(username='tony', email='tony@marvel.com', password='password', first_name='Tony', last_name='Stark'),
            UserProfile.objects.create_user(username='steve', email='steve@marvel.com', password='password', first_name='Steve', last_name='Rogers'),
            UserProfile.objects.create_user(username='bruce', email='bruce@dc.com', password='password', first_name='Bruce', last_name='Wayne'),
            UserProfile.objects.create_user(username='clark', email='clark@dc.com', password='password', first_name='Clark', last_name='Kent'),
        ]
        # Add users to teams
        marvel.members.add(users[0], users[1])
        dc.members.add(users[2], users[3])

        # Create Activities

        activities = [
            Activity.objects.create(user=users[0], activity_type='running', duration_minutes=30, calories_burned=300, distance_km=5),
            Activity.objects.create(user=users[1], activity_type='cycling', duration_minutes=60, calories_burned=600, distance_km=20),
            Activity.objects.create(user=users[2], activity_type='swimming', duration_minutes=45, calories_burned=450, distance_km=2),
            Activity.objects.create(user=users[3], activity_type='running', duration_minutes=50, calories_burned=500, distance_km=10),
        ]

        # Create Leaderboard entries

        Leaderboard.objects.create(user=users[0], points=100, rank=1, calories_burned=300, total_workouts=1)
        Leaderboard.objects.create(user=users[1], points=90, rank=2, calories_burned=600, total_workouts=1)
        Leaderboard.objects.create(user=users[2], points=110, rank=1, calories_burned=450, total_workouts=1)
        Leaderboard.objects.create(user=users[3], points=95, rank=2, calories_burned=500, total_workouts=1)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
