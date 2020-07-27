import os

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from psycopg2 import connect
from sendgrid import SendGridAPIClient, Mail

from .models import Task


# Create your views here.

def lists(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'tasks.html', context)


def mylists(request):
    tasks = Task.objects.all()
    for task in tasks:
        task = str(task.id) + ' ' + task.title
        return HttpResponse(task)



