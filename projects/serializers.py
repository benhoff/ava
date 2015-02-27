from django.forms import widgets
from rest_framework import serializers
from projects.models import Project
from django.contrib.auth.models import User

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    description = serializers.HyperlinkedIdentityField(view_name='project-description', format='html')

    class Meta:
        model = Project
        fields = ('url', 'title', 'description', 'owner')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(many=True, view_name='project-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'projects')


