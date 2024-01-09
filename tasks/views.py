from django.shortcuts import render, redirect
# Models
from .models import Task

# Create your views here.
def list_tasks(request):
    return render(request, 'list_tasks.html')

def create_tasks(request):
    # print(request.POST)
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')