from rest_framework import serializers

from rest_extensions.relations import HyperlinkedNestedRelatedField

from projects.models import Project
from ideas.models import Idea

# TODO: Think about how we really want to get at this information
from ideas.serializers import IdeaSerializer
from discussions.serializers import DiscussionSerializer

class ProjectSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')

    # Is this better suited to use as a 'edge'
    ideas = IdeaSerializer(many=True)
    discussions = DiscussionSerializer(many=True)
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
                'ideas',
                'discussions')
