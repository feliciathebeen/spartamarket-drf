from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'nick_name', 'birthday', 'gender', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            nick_name=validated_data['nick_name'],
            birthday=validated_data['birthday'],
            gender=validated_data['gender'],
            password=validated_data['password']
        )
        return user



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email', 'nick_name', 'birthday', 'gender']