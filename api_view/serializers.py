from rest_framework import serializers
from .models import AndroidApp,UserApp,Profile
from django.contrib.auth.models import User

class AdminView(serializers.ModelSerializer):
    class Meta:
        model=AndroidApp
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Add other desired fields as needed
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class UserAppSerializer(serializers.ModelSerializer):
    
    # app = AdminView()  # Nested serializer for the AndroidApp model
    class Meta:
        model = UserApp
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['total_points'] # Add the desired fields from the Profile model



class UserDataSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model = User
        fields = ['id','username', 'email','profile']  # Add other desired fields

