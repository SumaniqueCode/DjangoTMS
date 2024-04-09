from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    member_count = serializers.IntegerField(read_only=True)
    members= serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='profile-detail')
    manager= serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name= 'profile-detail' )   
    task_list = serializers.HyperlinkedRelatedField(read_only = True, many = True, view_name='tasklist-detail', source='lists' )
    """you can add source='' to give more meaning to the data otherwise the data can also be represented as
    lists = serializers.HyperlinkedRelatedField(read_only = True, many = True, view_name='tasklist-detail', )"""

    class Meta:
        model = House
        fields = ['id', 'url', 'name', 'created_at', 'updated_at', 'description','members', 'member_count', 'manager', 'task_list',
                  'points', 'completed_task', 'not_completed_task', 'image',]
        read_only_fields= ['points', 'completed_task', 'not_completed_task']