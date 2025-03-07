from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TaskForms


def lst_tasks(request):
    tasks = Tasks.objects.filter(parent=None)   # Главные задачи(без подзадач)
    return render(request, 'list_task.html', {'task': tasks})


# Создание новой задачи
def task_created(request):
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_task')   # После создания переходим на страницу с задачами
    else:
        form = TaskForms

    return render(request, 'create_task.html', {'form': form})


def task_edite(request, task_id):
    task = get_object_or_404(Tasks, task_id)

    if request.method == 'POST':
        form = TaskForms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_edite')
    else:
        form = TaskForms()
    return render(request, 'task_edite.html', {'form': form})