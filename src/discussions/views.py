from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_extensions.permissions import IsOwnerOrReadOnly

from discussions.models import Discussion
from discussions.serializers import DiscussionSerializer

class DiscussionViewSet(viewsets.ModelViewSet):
    """
    This viewset is nested under projects and provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions
    """

    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly)

    def list(self, request, project_pk=None):
        discussions = self.queryset.filter(project_id=project_pk)
        serializer = DiscussionSerializer(discussions,
                                          many=True,
                                          context={'request':request})

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
