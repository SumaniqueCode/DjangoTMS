from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
   user = serializers.HyperlinkedRelatedField(read_only= True, many= False, view_name='user-detail')
   house = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='house-detail')
   class Meta:
       model = Profile
       fields =['url', 'id', 'user', 'image','house']
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False) #it has no validations
    old_password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)
    profile = ProfileSerializer(read_only = True)

    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password', None)
        if request_method == 'POST':
            if password == None:
                raise serializers.ValidationError({'message':'Password is required.'})
        elif request_method  == 'PUT' or request_method == 'PATCH':
            old_password = data.get('old_password')
            if password != None and old_password == None:
                raise serializers.ValidationError({'message':'Old Password is required to change the password.'})
            
        return data

    def create(self, validated_data):   #for password validation from user model
        password = validated_data.pop('password') 
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
    
    def update(self, instance, validated_data):  #to allow only the owner to modify his profile
        try:
            user = instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                old_password = validated_data.pop('old_password')
                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception("Old Password is incorrect")
                
                user.save()
        except Exception as err:
            raise serializers.ValidationError(err)
        
        #To keep other data unchanged 
        return super(UserSerializer, self).update(instance,validated_data)

    class Meta:
        model = User
        fields = ['url', 'id', 'username','email','first_name', 'last_name','password', 'old_password','profile',]