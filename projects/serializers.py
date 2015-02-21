from django.forms import widgets
from rest_framework import serializers
from projects.models import Project

class ProjectSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=30)
    description = serializers.CharField()
    linenos = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new 'Project' instance, given the validated data.
        """
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Project' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
