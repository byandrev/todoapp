from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerialize


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialize
