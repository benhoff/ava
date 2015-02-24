from projects.models import Project
from projects.serializers import ProjectSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProjectList(APIView):
    """
    List all projects or create a new project.
    """
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
    """
    Retrieve, update, or delete a project instance.
    """
    def get_object(self, primary_key):
        try:
            return Project.objects.get(pk=primary_key)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, primary_key, format=None):
        project = self.get_object(primary_key)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, primary_key, format=None):
        project = self.get_object(primary_key)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, primary_key, format=None):
        project = self.get_object(primary_key)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
