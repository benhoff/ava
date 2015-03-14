from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(many=True, view_name='project-detail', read_only=True)
    model = User
    fields = ('url', 'username', 'projects')
