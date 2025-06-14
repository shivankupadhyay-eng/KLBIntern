from rest_framework import serializers
from django.contrib.auth import get_user_model 

User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','telegram_id','telegram_username']
