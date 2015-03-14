from projects.models import Project
from rest_framework import serializers
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from ideas.models import Idea

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())

    #idea_list = serializers.HyperlinkedIdentityField(view_name='idea-list', many=True)

    class Meta:
        model = Project
        fields = ('url', 'title', 'description', 'user', 'status', 'idea_list')
