from comments.models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Comment
        fields = ('owner', 'content', 'idea', 'votes')

