from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserCreationView

router = routers.DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/users", UserCreationView.as_view()),
    path("api/", include(router.urls)),
]
