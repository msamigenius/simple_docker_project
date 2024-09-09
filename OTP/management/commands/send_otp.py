from django.core.management.base import BaseCommand
# from OTP.models import OTPModel  # Adjust the import according to your models
# from OTP.tasks import send_otp_email_task

from OTP.tasks import send_otp_email_task
class Command(BaseCommand):
    help = 'Send OTP to a user'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str)
        parser.add_argument('otp', type=int)

    def handle(self, *args, **options):
        email = options['email']
        otp = options['otp']
        # Add logic to send OTP here
        send_otp_email_task(email,otp)
        self.stdout.write(self.style.SUCCESS(f'Successfully sent OTP {otp} to {email}'))
