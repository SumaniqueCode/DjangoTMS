from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=('id','name', 'description','status', 'created_by', 'completed_by', 'completed_at', 'created_at', 'updated_at', )

admin.site.register(Task, TaskAdmin)
