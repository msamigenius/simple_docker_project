# tasks/views.py
from django.shortcuts import render
from .tasks import send_email_task
from django.http import HttpResponse

def trigger_email(request):
    send_email_task.delay()  # Use delay() to run the task asynchronously
    # r    send_email_task.delay()
    return HttpResponse("Task has been triggered!")
