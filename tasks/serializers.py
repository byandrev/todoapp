from rest_framework import serializers
from .models import Task
from users.models import User


class TaskSerialize(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "status",
            "description",
            "created_at",
            "limit_date",
            "user_id",
        )
