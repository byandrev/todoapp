from django.http import JsonResponse
from django.core.serializers import serialize
from .models import User


def index(request):
    users = User.objects.filter(is_superuser=False)
    data = serialize(
        "python", users, fields=["username", "email", "date_joined", "photo"]
    )
    return JsonResponse(data, safe=False)
