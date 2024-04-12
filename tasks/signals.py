from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import datetime

from .models import COMPLETED, NOT_COMPLETED

from .models import Task

@receiver(post_save, sender=Task)
def update_house_points(sender,  instance, **kwargs):
    house = instance.task_list.house
    if instance.status == COMPLETED:
        house.points += 10
    elif house.status == NOT_COMPLETED:
        if house.points >= 10:
            house.points -= 10
    house.save()
    
@receiver(post_save, sender=Task)
def update_task_list_status(sender, instance, **kwargs):
    task_list = instance.task_list
    is_complete = True
    for task in task_list.tasks.all(): 
        if task.status != COMPLETED:
            is_complete = False
            break
    task_list.status = COMPLETED if is_complete == True else NOT_COMPLETED
    task_list.completed_at = datetime.now() if is_complete == True else None
    task_list.save()           