from rest_framework import serializers
from .models import UserInfo

class UserInfoserializer(serializers.Serializer):
    fname = serializers.CharField(max_length=30)
    lname = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=40)
    password = serializers.CharField(max_length=30)

    def create(self,validate_data):
        return UserInfo.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.fname = validate_data.get('fname',instance.fname)
        instance.lname = validate_data.get('lname',instance.lname)
        instance.username = validate_data.get('username',instance.username)
        instance.email = validate_data.get('email',instance.email)
        instance.password = validate_data.get('password',instance.password)
        instance.save()
        return instance