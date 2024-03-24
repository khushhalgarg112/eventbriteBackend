from rest_framework import serializers

from .models import Auth, Event, Like, Person


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ['email', 'password']
# This is for registeration purpose that why its field is all
class AuthRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
