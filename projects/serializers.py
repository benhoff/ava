from rest_framework import serializers

from rest_extensions.relations import HyperlinkedNestedRelatedField

from projects.models import Project
from ideas.models import Idea
from ideas.serializers import IdeaSerializer

class ProjectSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')
    ideas = IdeaSerializer(many=True)
    class Meta:
        model = Project
        fields = (
                'id',
                'title', 
                'url', 
                'description', 
                'status', 
                'ownername', 
                'owner',
                'ideas')

class ProjectDetailSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')

    # Desired behavior is to directly include the idea serializer 

    idea_list = serializers.PrimaryKeyRelatedField(
            queryset=Idea.objects.all(),
            many=True,
            source='ideas')

    class Meta:
        model = Project
        fields = ('title', 
                  'url', 
                  'description', 
                  'ownername',
                  'owner', 
                  'status',
                  'idea_list')
