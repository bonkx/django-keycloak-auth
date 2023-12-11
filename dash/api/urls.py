from django.urls import include, path
from rest_framework import routers

from .views import auth, users

router = routers.SimpleRouter()
router.register(r'users', users.UserViewSet)

urlpatterns = [
    # Public Routes
    path('pub/users/', users.list_users),
    path('register/', auth.register),

    # Auth Routes
    path('me/', users.me),
    path('', include(router.urls)),  # type: ignore
]
