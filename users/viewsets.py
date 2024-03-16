from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly

class UserViewsets(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

# # if we had defined
#  class userViewsets(viewsets.Viewset):
# # we had to define function for each task like
#     def list(self, request):
#         //
#     def retrive(self, request):
#         //    