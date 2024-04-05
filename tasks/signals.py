from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Task

@receiver(pre_save, sender=Task)
def create_task_creator(sender,  instance, **kwargs):
    Task.created_by = instance.id