from django.forms import widgets
from projects.models import Project
from rest_framework import serializers
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ('url', 'id', 'title', 'description', 'owner', 'status')
