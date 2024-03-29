from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'url', 'name', 'created_at', 'updated_at', 'description', 'manager', 'points', 'completed_task', 'not_completed_task', 'image',]