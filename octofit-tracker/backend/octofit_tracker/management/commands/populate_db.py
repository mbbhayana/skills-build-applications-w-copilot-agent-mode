from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.filter(pk__isnull=False).delete()
        Team.objects.filter(pk__isnull=False).delete()
        Activity.objects.filter(pk__isnull=False).delete()
        Leaderboard.objects.filter(pk__isnull=False).delete()
        Workout.objects.filter(pk__isnull=False).delete()


        # Create Teams
        marvel = Team(name='marvel', description='Marvel Team')
        marvel.save()
        dc = Team(name='dc', description='DC Team')
        dc.save()

        # Create Users
        tony = User(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        tony.save()
        steve = User(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        steve.save()
        bruce = User(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        bruce.save()
        clark = User(email='clark@kent.com', name='Clark Kent', team=dc.name)
        clark.save()


        # Create Activities (use user_id)
        Activity.objects.create(user_id=tony.id, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user_id=steve.id, type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user_id=bruce.id, type='cycle', duration=60, date=timezone.now().date())
        Activity.objects.create(user_id=clark.id, type='run', duration=50, date=timezone.now().date())

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Pullups', description='Do 10 pullups', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='easy')


        # Create Leaderboard (use team_id)
        Leaderboard.objects.create(team_id=marvel.id, points=150)
        Leaderboard.objects.create(team_id=dc.id, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
