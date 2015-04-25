from rest_framework import serializers
from blog.models import Post
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')

    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = (
                'id',
                'title',
                'owner',
                'ownername',
                'body',
                'created',
                'edited',
                'project',
                'comments')
