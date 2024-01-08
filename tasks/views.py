from django.shortcuts import render, redirect

# Create your views here.
def list_tasks(request):
    return render(request, 'list_tasks.html')

def create_tasks(request):
    print(request.POST)
    return redirect('/tasks/')