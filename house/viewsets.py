from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import House
from . serializers import HouseSerializer
from .permission import IsHouseManagerOrNot

class HouseViewSets(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsHouseManagerOrNot,]

    @action(detail=True, methods=['post'], name='Join', permission_classes= []) 
    #Empty permission classes overrides the permission classes that are applied before
    def join(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.profile
            if(user_profile.house == None):
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif(user_profile in house.members.all()):
                return Response({'message ': "User already exist in this house"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message ': 'Already a member of another house'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True, methods=['post'], name='Leave', permission_classes= []) 
    def leave(self, request, pk=None):
        try:
            house = self.get_object()
            user_profile = request.user.profile
            
            if(user_profile.house in house.members.all()):
                user_profile.house = None
                user_profile.save()
                return Response({'message ': 'Left house'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message ': 'User is not the member of this house.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True, methods=['post'], name='Remove Member')
    def  remove_member(self, request, pk=None):
        try:
            house = self.get_object()
            user_id = request.data.get('user_id', None)
            if(user_id == None):
                return Response({'user_id':'User id Not provided'}, status=status.HTTP_400_BAD_REQUEST)
            user_profile = User.objects.get(pk=user_id).profile
            house_member = house.members
            if(user_profile in house_member.all()):
                house_member.remove(user_profile)
                house.save()
                return Response({'message ': 'User Removed from the house.'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message ': 'User is not the member of this house.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as err:
            return Response({'message ': err},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
