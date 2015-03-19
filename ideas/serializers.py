from ideas.models import Idea
from rest_framework import serializers
from projects.models import Project
from comments.models import Comment
from django.contrib.auth.models import User

class IdeaDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', 
                                                queryset=User.objects.all())

    project = serializers.HyperlinkedRelatedField(view_name='project-detail',
                                                  queryset=Project.objects.all())

    """
    comments = serializers.RelatedField(view_name='comment-detail',
                                        queryset=Comment.objects.all())
    """

    class Meta:
        model = Idea
        fields = ('url','owner',  'description', 'votes', 'created', 'edited', 'project')

class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', 
                                                queryset=User.objects.all())

    project = serializers.HyperlinkedRelatedField(view_name='project-detail',
                                                  queryset=Project.objects.all())

    class Meta:
        model = Idea
        fields = ('url', 'owner', 'project', 'description', 'votes')
