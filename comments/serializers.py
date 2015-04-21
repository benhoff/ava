from comments.models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')     

    class Meta:
        model = Comment
        fields = (
                'id',
                'ownername',
                'owner', 
                'content')

