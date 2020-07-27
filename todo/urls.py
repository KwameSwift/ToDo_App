from django.urls import path
from .views import lists, mylists
from .models import send_update

urlpatterns =[
    path('', lists, name='tasks_list'),
    path('json', mylists, name='tasks_list'),
    path('update', send_update, name='Send_Update'),
]