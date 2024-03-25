from rest_framework import routers
from .viewsets import UserViewsets, ProfileViewsets

app_name = "users"

router = routers.DefaultRouter()
router.register('users', UserViewsets)
router.register('profiles', ProfileViewsets)