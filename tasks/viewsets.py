from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsTaskManager

class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes= [IsTaskManager, ]