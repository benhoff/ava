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
    
    ideas_count = serializers.ReadOnlyField(source='ideas.count')

    ideas_list = serializers.HyperlinkedRelatedField(source='project.ideas', view_name='ideas-list', read_only=True)

    class Meta:
        model = Project
        fields = ('title', 'url', 'description', 'status', 'ownername', 'owner_url','ideas_count', 'ideas-list')

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
