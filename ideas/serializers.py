from ideas.models import Idea
from rest_framework import serializers
from projects.models import Project
from comments.serializers import CommentSerializer

class IdeaSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='owner.username')
    
    comments = CommentSerializer(many=True)

    class Meta:
        model = Idea
        fields = (
                'id',
                'title',  
                'description', 
                'votes', 
                'username', 
                'created', 
                'edited', 
                'project',
                'comments')
