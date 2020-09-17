from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model

class Signup(ModelSerializer):
    
    password = serializers.CharField(write_only = True)

    class Meta:
        model : User
        fields = ['username', 'password', 'email','phone_number']

    def create(self, data):
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


