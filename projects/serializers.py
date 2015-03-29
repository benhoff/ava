from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import serializers
from rest_framework_nested import relations

from projects.models import Project
from users.serializers import UserSerializer
from ideas.serializers import IdeaSerializer
from ideas.models import Idea


class HyperlinkedIdeaList(serializers.HyperlinkedRelatedField):
    def to_representation(self, value):
        ideas = value.all()
        print(ideas)
        results = []
        for idea in ideas:
            results.append(reverse('idea-list', kwargs={'project_pk' : idea.project.pk}))
        return results

class HyperlinkedIdeaField(serializers.HyperlinkedRelatedField):

    def to_representation(self, value):
        url = reverse('idea-detail', kwargs={'project_pk': value.project.pk,
                                           'pk' : value.pk})
        return url

    def to_internal_value(self, data):
        print(type(data))
        return "dummy"

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    ownername = serializers.ReadOnlyField(source='owner.username')
    owner_url = serializers.HyperlinkedRelatedField(
            view_name='user-detail', 
            source='owner', 
            read_only=True)
    
    ideas_count = serializers.ReadOnlyField(source='ideas.count')
    ideas_list = HyperlinkedIdeaList(view_name='idea-list',
                                     read_only=True,
                                     source='ideas')
    class Meta:
        model = Project
        fields = ('title', 
                  'url', 
                  'description', 
                  'status', 
                  'ownername', 
                  'owner_url',
                  'ideas_count',
                  'ideas_list')

class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    ideas = HyperlinkedIdeaField(view_name='idea-detail',
                                 many=True,
                                 read_only=True)

    ownername = serializers.ReadOnlyField(source='owner.username')
    owner_url = serializers.HyperlinkedRelatedField(
            view_name='user-detail', 
            source='owner', 
            read_only=True)
 

    class Meta:
        model = Project
        fields = ('title', 'url', 'description', 'ownername','owner_url', 'status', 'ideas')
