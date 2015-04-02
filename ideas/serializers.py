from ideas.models import Idea
from rest_framework import serializers
from projects.models import Project
from comments.models import Comment
from rest_extensions.relations import HyperlinkedNestedIdentityField

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
    
    url = HyperlinkedNestedIdentityField(
            view_name='idea-detail',
            many=True,
            queryset=Idea.objects.all(),
            additional_reverse_kwargs={"project_pk" : 'project_id'}
            )

    class Meta:
        model = Idea
        fields = ('url', 'title', 'project', 'description', 'votes', 'username', 'user_link')
