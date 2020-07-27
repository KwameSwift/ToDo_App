import os

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.http import HttpResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.db import models

# Create your models here.

Category = [
    ('PROGRAMMING', 'PROGRAMMING'),
    ('BUGFIXING', 'BUGFIXING'),
    ('SOMETHING', 'SOMETHING'),
]


class Task(models.Model):
    creator_email = models.EmailField(max_length=255, unique=True, default='--------')
    responsible_email = models.EmailField(max_length=255, unique=True, default='------')
    title = models.CharField(max_length=255)
    category = models.CharField(choices=Category, max_length=55, default='-----')
    created_by_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Task')
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    done_on = models.DateTimeField(editable=False, null=True)
    responsible_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.title + ' is tasked to ' + str(self.responsible_username) + ' the done status of the task is ' \
               + str(self.status)


def send_update(created_by_username, responsible_username, **kwargs):

    if created_by_username == responsible_username:
        return HttpResponse('Successful')
    else:
        message = Mail(
            from_email='test@example.com',
            to_emails='charlestontaylor09@gmail.com',
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong>'
        )
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)


post_save.connect(send_update, sender=Task)
