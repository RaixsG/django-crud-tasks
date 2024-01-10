from django.shortcuts import render, redirect
# Models
from .models import Task

# Create your views here.
def list_tasks(request):
    # print(request.POST)
    taskToEdit = None
    tasks = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        taskToEdit = Task.objects.get(id=request.POST['id'])
    return render(request, 'list_tasks.html', {'tasks': tasks, 'taskToEdit': taskToEdit})

def create_tasks(request):
    print(request.POST)
    typeMethod = None
    print(request.POST['modo'])
    if request.POST['modo'] == 'guardar':
        task = Task(title=request.POST['title'], description=request.POST['description'])
        task.save()
    else:
        if Task.objects.filter(id=request.POST['id']).exists():
            Task.objects.filter(id=request.POST['id']).update(title=request.POST['title'], description=request.POST['description'])
    return redirect('/tasks/')

def delete_task(request, task_id):
    # print(task_id)
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')