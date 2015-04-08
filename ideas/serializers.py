from ideas.models import Idea
from rest_framework import serializers
from projects.models import Project
from comments.models import Comment
from rest_extensions.relations import HyperlinkedNestedIdentityField, HyperlinkedNestedRelatedField 

class NestedIdeaSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedNestedRelatedField(
            view_name='idea-detail',
            queryset = Idea.objects.all(), # TODO: think about passing in proj-pk
            many=True,
            source='ideas',
            lookup_url_kwarg='pk',
            additional_reverse_kwargs={"project_pk" : 'project_id'})

    class Meta:
        model = Idea
        fields = ('title',
                  'url',
                  'owner',
                  'votes',
                  'created',
                  'edited'
                  )

class IdeaDetailSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='owner.username')
    user_link = serializers.HyperlinkedRelatedField(
        view_name='user-detail', 
        source='owner',
        read_only=True)

    url = HyperlinkedNestedIdentityField(
            view_name='idea-detail',
            lookup_field="pk",
            additional_reverse_kwargs={'project_pk' : 'project_id'}
            )

    project = serializers.HyperlinkedRelatedField(view_name='project-detail',
                                                  queryset=Project.objects.all())
    """
    comments = serializers.HyperlinkedRelatedField(view_name='comment-detail',
                                                   queryset=Comment.objects.all())
    """
    class Meta:
        model = Idea
        fields = ('url',
                  'title',  
                  'description', 
                  'votes', 
                  'username', 
                  'user_link', 
                  'created', 
                  'edited', 
                  'project',
                  'comment_set')

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
            lookup_field="pk",
            additional_reverse_kwargs={'project_pk' : 'project_id'}
            )

    class Meta:
        model = Idea
        fields = ('url', 'title', 'project', 'description', 'votes', 'username', 'user_link')
