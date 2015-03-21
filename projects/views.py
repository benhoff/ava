from projects.models import Project
from projects.serializers import ProjectSerializer, ProjectDetailSerializer
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
    # TODO: Set permissions so that users can't create projects under other user names
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        if pk is None:
            serializer = ProjectSerializer(project)
        else:
            serializer =  ProjectDetailSerializer(project, 
                                                  context={'request':request})

        return Response(serializer.data)
