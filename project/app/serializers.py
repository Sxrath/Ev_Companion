from rest_framework import serializers
from .models import Chargingspot,Location, Post,Reservation,User,Feedback,Reply

class Chargingspotserializer(serializers.ModelSerializer):
    class Meta:
        model=Chargingspot
        fields='__all__'

class Locationserializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'

class Reservatioinserializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields=['starttime','endtime','chargingspot']

class Userserilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
         
class feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['content']

class Replyserializer(serializers.ModelSerializer):
    class Meta:
        model=Reply
        fields='__all__'