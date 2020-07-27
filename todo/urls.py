from django.urls import path
from .views import lists, mylists

urlpatterns =[
    path('', lists, name='tasks_list'),
    path('json', mylists, name='tasks_list'),
]