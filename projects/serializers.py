from projects.models import Project
from rest_framework import serializers
from django.contrib.auth.models import User
from ideas.models import Idea
from users.serializers import UserSerializer
from ideas.serializers import IdeaSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'title', 'description', 'status', 'user')
        read_only_fields = fields

class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    ideas = IdeaSerializer(many=True,
                           read_only=True)

    class Meta:
        model = Project
        fields = ('url', 'title', 'description', 'user', 'status', 'ideas')
