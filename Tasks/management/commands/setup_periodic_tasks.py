from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class Command(BaseCommand):
    help = 'Setup periodic tasks for Celery'

    def handle(self, *args, **kwargs):
        # Create an interval schedule
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=2,
            period=IntervalSchedule.MINUTES,
        )

        # Create or update a periodic task
        PeriodicTask.objects.update_or_create(
            name='send_email_task_every_2_minutes',
            defaults={
                'task': 'Tasks.tasks.send_email_task',
                'interval': schedule,
                'enabled': True,
                'description': 'Sends an email every 2 minutes',
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully setup periodic tasks'))
