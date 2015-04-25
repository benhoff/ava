from rest_framework import serializers

from rest_extensions.relations import HyperlinkedNestedRelatedField

from projects.models import Project
from ideas.models import Idea


class ProjectSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = (
                'id',
                'title', 
                'url', 
                'description', 
                'status', 
                'ownername', 
                'owner')
