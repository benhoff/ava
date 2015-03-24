from projects.models import Project
from rest_framework import serializers
from django.contrib.auth.models import User
from ideas.models import Idea
from users.serializers import UserSerializer
from ideas.serializers import IdeaSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')
    owner_url = serializers.HyperlinkedRelatedField(
            view_name='user-detail', 
            source='owner', 
            read_only=True)

    class Meta:
        model = Project
        fields = ('title', 'url', 'description', 'status', 'ownername', 'owner_url')

class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    ideas = IdeaSerializer(many=True,
                           read_only=True)

    ownername = serializers.ReadOnlyField(source='owner.username')
    owner_url = serializers.HyperlinkedRelatedField(
            view_name='user-detail', 
            source='owner', 
            read_only=True)
 

    class Meta:
        model = Project
        fields = ('title', 'url', 'description', 'ownername','owner_url', 'status', 'ideas')
