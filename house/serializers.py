from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    member_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = House
        fields = ['id', 'url', 'name', 'created_at', 'updated_at', 'description','member_count', 'manager', 'points', 'completed_task', 'not_completed_task', 'image',]
        read_only_fields= ['points', 'completed_task', 'not_completed_task']