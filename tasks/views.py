from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Task

def index(request):
    tasks = Task.objects.all()
    data = serialize('python', tasks)
    #context = {'tasks': tasks}
    #return HttpResponse(tasks)
    return JsonResponse(data, safe=False)
