from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class meta:
        user = User
        fields = ['url', 'id', 'username','email','first_name', 'last_name']