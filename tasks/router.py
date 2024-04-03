from rest_framework import routers

from .viewsets import TaskViewSets

app_name = 'Task'

router = routers.DefaultRouter()
router.register('manage', TaskViewSets)