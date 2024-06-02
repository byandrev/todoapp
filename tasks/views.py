from tasks.serializers import TaskSerializer
from .models import Task
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [OrderingFilter]
    ordening_fields = ["priority"]


def get_queryset(self):
    return self.request.user.tasks.all()
