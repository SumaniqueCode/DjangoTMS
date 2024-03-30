from rest_framework import routers
from .viewsets import HouseViewSets

app_name = "House"

router = routers.DefaultRouter()
router.register('manage', HouseViewSets)