from django.shortcuts import render, redirect
from .models import Task

def index(request):
    todo_list = Task.objects.filter(completed=False)
    completed_list = Task.objects.filter(completed=True)
    return render(request, 'todolist/index.html', {'todo_list': todo_list, 'completed_list': completed_list})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        new_task = Task.objects.create(title=title)
        return redirect('index')

def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')
