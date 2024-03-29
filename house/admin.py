from django.contrib import admin
from .models import House

class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'description', 'manager', 'points', 'completed_task', 'not_completed_task',)

admin.site.register(House, HouseAdmin)
