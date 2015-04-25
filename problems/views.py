from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions
from rest_framework.response import Response

from rest_extensions.permissions import IsOwnerOrReadOnly

from problems.models import Problem
from problems.serializers import ProblemSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    """
    This viewset is nested under projects and provides 'list', 'create', 
    'retrieve', 'update', and 'destroy' actions
    """
    queryset = Problem.objects.all()
    serialzier_class = ProblemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def list(self, request, project_pk=None):
        problems = self.queryset.filter(project_id=project_pk)
        serializer = ProblemSerializer(problems,
                                       many=True,
                                       context={'request':request})

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
