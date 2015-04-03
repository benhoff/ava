from ideas.models import Idea
from ideas.serializers import IdeaSerializer, IdeaDetailSerializer
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

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Idea.objects.all()
        idea = get_object_or_404(queryset, pk=pk, project_id=project_pk)

        if pk is None:
            serializer = IdeaSerializer(idea)
        else:
            serializer = IdeaDetailSerializer(idea, 
                                              context={'request':request})

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IdeaViewSet(viewsets.ModelViewSet):
    """
    This viewset automagically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions
    """
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = Idea.objects.all()
        idea = get_object_or_404(queryset, pk=pk)
        if pk is None:
            serializer = IdeaSerializer(idea)
        else:
            serializer = IdeaDetailSerializer(idea, 
                                              context={'request':request})

        return Response(serializer.data)
