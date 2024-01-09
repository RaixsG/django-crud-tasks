from django.shortcuts import render, redirect
# Models
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {'tasks': tasks})

def create_tasks(request):
    # print(request.POST)
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    # print(task_id)
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')

def edit_task(request, task_id):
    task = Task.objects.filter(id=task_id).update(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')