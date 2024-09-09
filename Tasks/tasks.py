# # tasks/tasks.py
# from celery import shared_task
# from django.core.mail import send_mail
# from django.utils.timezone import now

# @shared_task
# def send_email_task():
#     send_mail(
#         'Scheduled Email',
#         'This is an automated email sent by Celery!',
#         'msamiullahmashfaqtahir@gmail.com',
#         ['msamimashfaqtahir@gmail.com'],
#         fail_silently=False,
#     )
#     print(f'Email sent at {now()}')



from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
import logging
from management_celery import settings

logger = logging.getLogger(__name__)

@shared_task
def send_email_task():
    subject = 'SMS Sent Notification'
    message = f"How are you . This is celery message"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = settings.NOTIFICATION_EMAIL
    
    try:
        # Attempt to send the email
        send_mail(subject,message, from_email, [to_email])
        
        
        # Log the success
        logger.info(f'Email notification successfully sent for SMS to ')
    
    except Exception as e:
        # Log the error if email sending fails
        logger.error(f'Failed to send email')