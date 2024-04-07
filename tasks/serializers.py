from rest_framework import serializers
from .models import Task, TaskList, Attachments

class TaskListSerializer(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(read_only = True, many = False, view_name='house-detail')
    class Meta:
        model = TaskList
        fields = ['id','url', 'house', 'name', 'description','created_by','status', 'created_at', 'updated_at', 'completed_on',]
class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name= 'profile-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only= True, many= False, view_name='profile-detail')
    task_list = serializers.HyperlinkedRelatedField(read_only= True, many = False,view_name='tasklist-detail')
    
    class Meta:
        model = Task
        fields = ['id','url', 'task_list', 'name', 'description','status', 'created_by', 'completed_by', 'completed_at', 'created_at', 'updated_at',]
        
class AttachmentSerializer(serializers.ModelSerializer):
    
    task = serializers.HyperlinkedRelatedField(read_only = True, many = False, view_name= 'task-detail')
    class Meta:
        model = Attachments
        fields =  ['id','url', 'task', 'data', 'created_at', 'updated_at',]       