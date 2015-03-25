from ideas.models import Idea
from rest_framework import serializers
from projects.models import Project
from comments.models import Comment
from django.contrib.auth.models import User

class IdeaDetailSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='owner.username')
    user_link = serializers.HyperlinkedRelatedField(
        view_name='user-detail', 
        source='owner',
        read_only=True)

    project = serializers.HyperlinkedRelatedField(view_name='project-detail',
                                                  queryset=Project.objects.all())

    class Meta:
        model = Idea
        fields = ('url','title',  'description', 'votes', 'username', 'user_link', 'created', 'edited', 'project')

class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.HyperlinkedRelatedField(view_name='project-detail',
                                                  queryset=Project.objects.all())

    username = serializers.ReadOnlyField(source='owner.username')
    user_link = serializers.HyperlinkedRelatedField(
        view_name='user-detail', 
        source='owner',
        read_only=True)

    class Meta:
        model = Idea
        fields = ('url', 'title', 'project', 'description', 'votes', 'username', 'user_link')
