from rest_framework import viewsets, mixins, response
from rest_framework import status as taskStatus
from rest_framework.decorators import action
from django.utils import timezone

from .models import Task, TaskList, Attachments, COMPLETED, NOT_COMPLETED
from .serializers import TaskSerializer, TaskListSerializer, AttachmentSerializer
from .permissions import (
    IsTaskListManagerOrNot,
    IsTaskManagerOrNot,
    IsAttachmentManagerOrNot,
)


class TaskListViewSets(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [
        IsTaskListManagerOrNot,
    ]


class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        IsTaskManagerOrNot,
    ]

    def get_queryset(self):
        queryset = super(TaskViewSets, self).get_queryset()
        user_profile = self.request.user.profile
        updated_queryset = queryset.filter(created_by=user_profile)
        return updated_queryset

    @action(detail=True,methods=["patch"],name="Update Task")
    def update_task_status(self, request, pk=None):
        try:
            task = self.get_object()
            profile = request.user.profile
            status = request.data["status"]
            if status == NOT_COMPLETED:
                if task.status == COMPLETED:
                    task.status = NOT_COMPLETED
                    task.completed_by = None
                    task.completed_at = None
                else:
                    raise Exception("Task is already marked as not completed.")
            elif status == COMPLETED:
                if task.status == NOT_COMPLETED:
                    task.status = COMPLETED
                    task.completed_by = profile
                    task.completed_at = timezone.now()
                else:
                    raise Exception("Task is already marked as completed")
            else:
                raise Exception("Incorrect status provided")
            task.save()
            serializer = TaskSerializer(instance=task, context={"request": request})
            return response.Response(serializer.data, status=taskStatus.HTTP_200_OK)
        except Exception as err:
            return response.Response(
                {"message": str(err)}, status=taskStatus.HTTP_400_BAD_REQUEST
            )


class AttachmentViewSets(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [
        IsAttachmentManagerOrNot,
    ]
