from rest_framework import viewsets

from .models import Task, TaskList, Attachments
from .serializers import TaskSerializer, TaskListSerializer, AttachmentSerializer
from .permissions import IsTaskManager

class TaskListViewSets(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes= [IsTaskManager, ]
    
class AttachmentViewSets(viewsets.ModelViewSet):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentSerializer
