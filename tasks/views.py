from django.shortcuts import render, redirect
from .models import Task

class Views:
    def __init__(self):
        """Currently there is nothing to initialize."""
        pass

    def complete_task(self, request, index):
        """Marks a task of a particular index(in this case it is the ID of the task) as complete."""
        try:
            task = Task.objects.get(id=index)
            task.completed = True
            task.save()
        except Exception:
            pass
        return redirect('/all_tasks')

    def completed_tasks(self, request):
        """Displays all completed tasks."""
        completed_task = Task.objects.filter(completed=True, deleted=False)
        context = {'completed_tasks': completed_task}
        return render(request, 'completed_tasks.html', context)

    def all_tasks(self, request):
        """Displays pending and completed tasks."""
        pending_tasks = Task.objects.filter(completed=False, deleted=False)
        completed_tasks = Task.objects.filter(completed=True, deleted=False)
        context = {'pending_tasks': pending_tasks, 'completed_tasks': completed_tasks}
        return render(request, 'all_tasks.html', context)
    
    def tasks(self, request):
        """Displays pending tasks."""
        context = {"tasks": Task.objects.filter(completed=False, deleted=False)}
        return render(request, "tasks.html", context)

    def add_task(self, request):
        """Creates a new task and redirects to /all_tasks."""
        task = request.GET.get("task")
        task = Task.objects.create(title=task)
        if request.user.is_authenticated:
            task.user = request.user
        task.save()
        return redirect("/all_tasks")

    def delete_task(self, request, index):
        """Soft delete of a task with a given index."""
        task = Task.objects.get(id=index)
        task.deleted = True
        task.save()
        return redirect("/all_tasks")
