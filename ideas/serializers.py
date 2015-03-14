from ideas.models import Idea
from rest_framework import serializers
from projects.models import Project
from comments.models import Comment
from django.contrib.auth.models import User

class IdeaSerializer(serializers.ModelSerializer):

    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', 
                                                queryset=User.objects.all())

    """
    project = serializers.HyperlinkedIdentityField(view_name='project-detail',
                                                   queryset=Project.objects.all())

    comments = serializers.RelatedField(view_name='comment-detail',
                                        queryset=Comment.objects.all())
    """

    class Meta:
        model = Idea
        fields = ('owner', 'project', 'description', 'votes', 'comments')
