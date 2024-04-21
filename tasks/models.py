
from django.db import models
from django.db.models.functions import Now

class Status(models.TextChoices):
    COMPLETED = "Completed"
    PROGRESS = "In Progress"
    PENDING = "Pending"

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(default=Status.PENDING, max_length=100)
    limit_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(db_default=Now())