from projects.models import Project
from rest_framework import serializers
from django.contrib.auth.models import User
from ideas.models import Idea
from users.serializers import UserSerializer
from ideas.serializers import IdeaSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_url = serializers.HyperlinkedRelatedField(
            view_name='user-detail', 
            source='user', 
            read_only=True)

    class Meta:
        model = Project
        fields = ('title', 'url', 'description', 'status', 'username', 'user_url')

class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    ideas = IdeaSerializer(many=True,
                           read_only=True)

    username = serializers.ReadOnlyField(source='user.username')
    user_url = serializers.HyperlinkedRelatedField(
            view_name='user-detail', 
            source='user', 
            read_only=True)
 

    class Meta:
        model = Project
        fields = ('title', 'url', 'description', 'username','user_url', 'status', 'ideas')
