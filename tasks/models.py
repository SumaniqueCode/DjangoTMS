from django.db import models

COMPLETED = 'C'
NOT_COMPLETED = 'NC'
TASK_STATUS_CHOICES=[(COMPLETED, 'COMPLETED'), (NOT_COMPLETED, 'NOT COMPLETED')]

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey('users.profile', on_delete=models.SET_NULL, blank=True, null=True, related_name = 'created_task')
    completed_by = models.ForeignKey('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name= 'completed_task')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default=NOT_COMPLETED,)
    
    def __str__(self):
        return (f'{self.id} | {self.name}')
    

