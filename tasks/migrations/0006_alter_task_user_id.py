# Generated by Django 5.0.3 on 2024-05-09 13:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_task_user_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="user_id",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"is_admin": False},
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]