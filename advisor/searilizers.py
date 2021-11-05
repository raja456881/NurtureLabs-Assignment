from rest_framework import  serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.http.response import JsonResponse

class UserregisterSerializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ('email', 'username', 'password')


    def create(self, validated_data):
        user=User.objects.create_user(email=validated_data.get('email'), password=validated_data.get("password")
                                      ,username=validated_data.get("username"))
        user.is_staff=True
        user.is_active=True
        user.is_verified=True
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data=super().validate(attrs)
        data['user_id']=self.user.id
        return data

class AdvisorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Advisor
        fields="__all__"

class BookcallaadvisorSearilizers(serializers.ModelSerializer):
    advisor = AdvisorSerializers(read_only=True)
    user = UserregisterSerializers(read_only=True)
    class Meta:
        model=Bookcallaadvisor
        fields="__all__"

    def to_representation(self, instance):
        orignal_object = super().to_representation(instance)
        orignal_object.pop('user')
        return orignal_object

