from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework import generics

#TODO: Set up permissions to something sane

class RetrieveUserView(generics.RetrieveDestroyAPIView):
    """
    This endpoint presents the users in the system    
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ('username')
        
        

