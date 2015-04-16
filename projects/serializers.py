from rest_framework import serializers

from rest_extensions.relations import HyperlinkedNestedRelatedField

from projects.models import Project
from ideas.models import Idea
from ideas.serializers import IdeaSerializer

class ProjectSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')

    # Is this better suited to use as a 'edge'
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
