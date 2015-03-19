from projects.models import Project
from rest_framework import serializers
from django.contrib.auth.models import User
from ideas.models import Idea
from users.serializers import UserSerializer
from ideas.serializers import IdeaSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', 
                                               queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ('url', 'title', 'description', 'user', 'status')

class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    project = ProjectSerializer
    ideas = IdeaSerializer(many=True,
                           read_only=True)

    user = serializers.HyperlinkedRelatedField(view_name='user-detail',
                                               queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ('url', 'title', 'description', 'user', 'status', 'ideas')
