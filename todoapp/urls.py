from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet
from users.views import UserCreationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from users.views import UserCreationView, UserDetailView, UserUpdateView

router = routers.DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path("api/", include(router.urls)),
    path("api/users/", UserCreationView.as_view(), name="user_create"),
    path("api/user/", UserDetailView.as_view(), name="user_detail"),
    path("api/users/<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
]
