from django.shortcuts import render

from webapp.models import STATUS_CHOICES, Task


def index_view(request):
    return render(request, 'index.html')


def create_task(request):
    if request.method == "GET":
        context = {'status1': STATUS_CHOICES}
        return render(request, "create.html", context)
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        date = request.POST.get("date")
        new_task = Task.objects.create(description=description, status=status, date=date)
        context = {"new_task": new_task}
        return render(request, "create.html", context)


def tasks_view(request):

    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks_view.html', context)
