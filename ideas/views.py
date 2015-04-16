from ideas.models import Idea
from ideas.serializers import IdeaSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from ideas.permissions import IsOwnerOrReadOnly

class NestedIdeaViewSet(viewsets.ModelViewSet):
    """
    This viewset is nested under projects and provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions
    """
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def list(self, request, project_pk=None):
        idea = self.queryset.filter(project_id=project_pk)
        serializer = IdeaSerializer(idea,
                                    many=True,
                                    context={'request': request})

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
