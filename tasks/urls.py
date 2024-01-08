from django.urls import path
from .views import list_tasks, create_tasks

urlpatterns = [
    path('', list_tasks),
    path('new/', create_tasks)
]