from django.urls import path
from .views import list_tasks, create_tasks, delete_task, edit_task

urlpatterns = [
    path('', list_tasks),
    path('new/', create_tasks, name='create_tasks'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('edit_task/<int:task_id>', edit_task, name='edit_task')
]