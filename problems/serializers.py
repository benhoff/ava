from rest_framework import serializers
from problems.models import Problem
from comments.serializers import CommentSerializer

class ProblemSerializer(serializers.ModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.userneame')
    comments = CommentSerializer(many=True)

    class Meta:
        model = Problem
        fields = (
                'id',
                'title',
                'description',
                'ownername',
                'owner',
                'created',
                'edited',
                'project',
                'comments',)
