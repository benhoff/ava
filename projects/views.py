from projects.models import Project
from projects.serializers import ProjectSerializer, ProjectViewSerializer
from projects.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets, renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automagically provides 'list', 'create', 'retieve',
    'update', and 'destroy' actions.

    Additionally we also provide an extra 'highlight' action.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        if pk is None:
            serializer = ProjectSerializer(project)
        else:
            serializer =  ProjectViewSerializer(project)
        return Response(serializer)
