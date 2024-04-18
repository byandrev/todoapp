from django.http import HttpResponse

from .models import Task

def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return HttpResponse(tasks)
