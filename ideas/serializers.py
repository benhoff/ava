from ideas.models import Idea
from rest_framework import serializers
from projects.models import Project
from comments.serializers import CommentSerializer

class IdeaSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')
    
    # This is not an 'edge'
    comments = CommentSerializer(many=True)

    class Meta:
        model = Idea
        fields = (
                'id',
                'title',  
                'description', 
                'votes', 
                'ownername', 
                'owner',
                'created', 
                'edited', 
                'project',
                'comments')
