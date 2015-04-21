from rest_framework import serializers

from discussions.models import Discussion
from comments.serializers import CommentSerializer


class DiscussionSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')

    # TODO: Implement!
    #comments = CommentSerializer(many=True)

    class Meta:
        model = Discussion
        fields = (
                'id',
                'title',
                'description',
                'ownername',
                'owner',
                'created',
                'edited',
                'project',
                #'comments'
                )


