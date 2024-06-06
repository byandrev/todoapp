from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    search_fileds = ["name", "description"]
    fielteset_fields = ['status']

    def get_queryset(self):
        return self.request.user.tasks.all()
