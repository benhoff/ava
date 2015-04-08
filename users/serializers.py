from django.contrib.auth.models import User
from rest_framework import serializers
from rest_extensions.relations import HyperlinkedNestedRelatedField

class UserSerializer(serializers.HyperlinkedModelSerializer):
    ideas = HyperlinkedNestedRelatedField(
            view_name='idea-detail',
            read_only=True,
            many=True,
            lookup_url_kwarg='pk',
            additional_reverse_kwargs={"project_pk" : 'project_id'})

    class Meta:
        model = User
        fields = ('username', 'projects', 'ideas')
