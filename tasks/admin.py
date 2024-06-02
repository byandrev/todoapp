from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "priority",
        "user_id",
        "status",
        "limit_date",
        "created_at",
    ]
    search_fields = ["name"]
