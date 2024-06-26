from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "status",
            "priority",
            "description",
            "created_at",
            "limit_date",
        )

    def create(self, validated_data):
        validated_data["user_id"] = self.context["request"].user
        return super(TaskSerializer, self).create(validated_data)
