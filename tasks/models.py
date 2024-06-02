from django.db import models
from django.utils.timezone import now

from todoapp import settings


class StatusTask(models.TextChoices):
    COMPLETED = "Completed"
    PROGRESS = "In Progress"
    PENDING = "Pending"


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(
        default=StatusTask.PENDING, choices=StatusTask, max_length=100
    )
    limit_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        on_delete=models.RESTRICT,
        limit_choices_to={"is_superuser": False},
        related_name="tasks",
        null=True,
    )

    def __str__(self):
        return self.name
