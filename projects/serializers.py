from django.contrib.auth.models import User

from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework_nested import relations

from projects.models import Project
from users.serializers import UserSerializer
from ideas.serializers import IdeaSerializer
from ideas.models import Idea


class HyperlinkedIdeaList(serializers.HyperlinkedIdentityField):
    def to_representation(self, value):
        request = self.context.get('request', None)
        format = self.context.get('format', None)
        return self.get_url(value, self.view_name, request, format)

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
    ideas_list = serializers.HyperlinkedIdentityField(view_name='idea-list',
                                                      read_only=True,
                                                      source='ideas',
                                                      lookup_url_kwarg='idea-list')
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
