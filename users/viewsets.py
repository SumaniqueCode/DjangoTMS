from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from .serializers import UserSerializer, ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly
from .models import Profile

class UserViewsets(viewsets.ModelViewSet):
    #ModelViewSet contains all CRUD operation so we donot need to them specify all for each opearions
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewsets(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,): 
    #when we use generic viewsets we can specify specific operations for CRUD using mixins
    permission_classes = [IsProfileOwnerOrReadOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# # if we had defined
#  class userViewsets(viewsets.Viewset):
# # we had to define function for each task like
#     def list(self, request):
#         //
#     def retrive(self, request):
#         //    