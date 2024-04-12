from rest_framework import serializers
from .models import Task, TaskList, Attachments
from house.models import House

class TaskListSerializer(serializers.ModelSerializer):
    #queryset provides the ability to change the house too.
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many = False, view_name='house-detail')
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name= 'profile-detail')
    tasks = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='task-detail')

    class Meta:
        model = TaskList
        fields = ['id','url', 'house', 'name', 'description','created_by','status', 'created_at', 'updated_at', 'completed_at','tasks']
        read_only_fields = ['status', 'created_by','completed_at']
class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name= 'profile-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only= True, many= False, view_name='profile-detail')
    task_list = serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(), many = False,view_name='tasklist-detail')
    attachments =serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='attachments-detail')
    
    def validate_task_list(self, value):
        user_profile = self.context['request'].user.profile
        if value not in user_profile.house.lists.all():
            raise serializers.ValidationError("Tasklist doesnot belong to the house for which user is member")
        
        return value
    
    def create(self, validated_data):
        user_profile = self.context['request'].user.profile
        task = Task.objects.create(**validated_data)
        task.created_by = user_profile
        task.save()
        return task    
    class Meta:
        model = Task
        fields = ['id','url', 'task_list', 'name', 'description','status','attachments',
                  'created_by', 'completed_by', 'completed_at', 'created_at', 'updated_at',]
        read_only_fields=['created_by', 'completed_by', 'completed_at',]
        
class AttachmentSerializer(serializers.ModelSerializer):
    
    task = serializers.HyperlinkedRelatedField(queryset= Task.objects.all(), many = False, view_name= 'task-detail')
    
    def validate(self, attrs):
        user_profile = self.context['request'].user.profile
        task = attrs['task']
        task_list = TaskList.objects.get(task__id__exact = task.id)
        if task_list  not in user_profile.house.lists.all():
            raise serializers.ValidationError({"task":"This task does not belong to the house for which user is member"})
        
        return attrs

    class Meta:
        model = Attachments
        fields =  ['id','url', 'task', 'data', 'created_at', 'updated_at',]       