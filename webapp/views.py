
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from webapp.models import STATUS_CHOICES, Task

from hw45KimL.webapp.forms import TaskForm


def index_view(request):
    return render(request, 'index.html')


def create_task(request):
    if request.method == "GET":
        form=TaskForm()
        context = {'stat1': STATUS_CHOICES, 'form':form}
        return render(request, "create.html", context)
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            date = form.cleaned_data.get("date")
            new_task = Task.objects.create(description=description, status=status, date=date, title=title)
            return redirect("task_view", pk=new_task.pk)
        return render(request, "create.html", {'form':form})

def tasks_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks_view.html', context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task
    }
    return render(request, 'task_view.html', context)

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        context = {'task': task, "stat1":STATUS_CHOICES }
        return render(request, "update.html", context)
    else:
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.status = request.POST.get("status")
        task.date = request.POST.get("date")
        task.save()
        print(task)
        return redirect("task_view", pk=task.pk)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {'task':task})
    else:
        task.delete()
        return redirect("tasks_view")


