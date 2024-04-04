from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name= 'profile-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only= True, many= False, view_name='profile-detail')
    
    class Meta:
        model = Task
        fields = ['id','name', 'description','status', 'created_by', 'completed_by', 'completed_at', 'created_at', 'updated_at',]