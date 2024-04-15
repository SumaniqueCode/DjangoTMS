from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from .models import Task, TaskList, Attachments
from .serializers import TaskSerializer, TaskListSerializer, AttachmentSerializer
from .permissions import IsTaskListManagerOrNot, IsTaskManagerOrNot, IsAttachmentManagerOrNot


class TaskListViewSets(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsTaskListManagerOrNot,]

class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTaskManagerOrNot,]
    
    def get_queryset(self):
        queryset= super(TaskViewSets, self).get_queryset()
        user_profile = self.request.user.profile
        updated_queryset = queryset.filter(created_by=user_profile)
        return updated_queryset
    @action(detail=True, methods=['patch'])
    def update_task_status(self, request, pk=None):
        try:
            task = self.get_object()
            profile = request.user.profile
            status = request.data['status']
        except Exception as err:
            pass
class AttachmentViewSets(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAttachmentManagerOrNot,]
