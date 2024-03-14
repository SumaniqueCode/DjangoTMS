from rest_framework import routers
from .viewsets import UserViewsets

app_name = "users"

router = routers.DefaultRouter()
router.register('users', UserViewsets)