from rest_framework import routers
from .viewsets import HouseViewSets


router = routers.DefaultRouter()
router.register('manage', HouseViewSets)