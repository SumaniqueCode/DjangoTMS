from django.contrib import admin
from .models import Task, TaskList, Attachments

class TaskListAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
class TaskAdmin(admin.ModelAdmin):
    list_display=('id','name', 'description','status', 'created_by', 'completed_by', 'completed_at', 'created_at', 'updated_at', )

class TaskAttachmentsAdmin(admin.ModelAdmin):
    list_display = ('id',)   
    
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin,)
admin.site.register(Attachments, TaskAttachmentsAdmin)
