from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Category = [
    ('PROGRAMMING', 'PROGRAMMING'),
    ('BUGFIXING', 'BUGFIXING'),
    ('SOMETHING', 'SOMETHING'),
]


class Task(models.Model):
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
