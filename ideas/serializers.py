from ideas.models import Idea
from rest_framework import serializers
from projects.models import Project
from comments.models import Comment
from django.contrib.auth.models import User

class IdeaSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', 
                                                queryset=User.objects.all())

    project = serializers.HyperlinkedIdentityField(view_name='project-detail')
    """
    comments = serializers.RelatedField(view_name='comment-detail',
                                        queryset=Comment.objects.all())
    """

    class Meta:
        model = Idea
        fields = ('url', 'owner', 'project', 'description', 'votes', 'created', 'edited')
