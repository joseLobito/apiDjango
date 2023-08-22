from rest_framework import serializers
from users.models import *

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username','password']
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        isinstance = self.Meta.model(**validated_data)
        if password is not None:
            isinstance.set_password(password)
        isinstance.save()
        return isinstance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username','first_name','last_name']

class UserUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'first_name','last_name']