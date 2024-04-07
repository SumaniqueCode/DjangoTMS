from rest_framework import routers

from .viewsets import TaskViewSets, TaskListViewSets, AttachmentViewSets

app_name = 'Task'

router = routers.DefaultRouter()
router.register('task-list', TaskListViewSets)
router.register('task', TaskViewSets)
router.register('attachments', AttachmentViewSets)
