from django.db import models
from uuid import uuid4
from django.utils.deconstruct import deconstructible
import os

COMPLETED = 'C'
NOT_COMPLETED = 'NC'
TASK_STATUS_CHOICES=[(COMPLETED, 'COMPLETED'), (NOT_COMPLETED, 'NOT COMPLETED')]

@deconstructible
class GenerateAttachmentPath(object):
    def __init__(self):
        pass
    
    def __call__(self, instance, filename):
        ext = filename.split( '.')[-1]
        path = f'media/task/{instance.id}/attachments'
        name = f'{instance.id}.{ext}'
        return os.path.join(path, name)

attachment_path = GenerateAttachmentPath()        
class TaskList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null= True)
    created_by = models.ForeignKey('users.Profile', on_delete=models.SET_NULL, blank=True, null= True, related_name = 'lists')
    house = models.ForeignKey('house.House', on_delete=models.CASCADE, blank=True, null=True, related_name='lists')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default=NOT_COMPLETED)
    
    def __str__(self):
        return (f'{self.id} | {self.name}')
    

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    task_list = models.ForeignKey('tasks.TaskList', blank=True, null=True, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey('users.profile', on_delete=models.SET_NULL, blank=True, null=True, related_name = 'created_task')
    completed_by = models.ForeignKey('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name= 'completed_task')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default=NOT_COMPLETED,)
    
    def __str__(self):
        return (f'{self.id} | {self.name}')
    
class Attachments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    data = models.FileField(upload_to=attachment_path)
    task = models.ForeignKey('tasks.Task',  on_delete= models.CASCADE, related_name='attachments')
    
    def __str__(self):
        return (f'{self.id} | {self.task}')
    