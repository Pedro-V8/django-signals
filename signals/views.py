from http import server
from signals.models import Profile
from signals.serializers import UserSerializer

from rest_framework import viewsets

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
