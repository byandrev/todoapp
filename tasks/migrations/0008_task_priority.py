# Generated by Django 5.0.3 on 2024-05-23 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0007_alter_task_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="priority",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
