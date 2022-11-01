import email
from rest_framework import serializers
from signals.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = ('username' , 'email')
