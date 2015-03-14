from ideas.models import Idea
from ideas.serializers import IdeaSerializer
from rest_framework import viewsets

class IdeaViewSet(viewsets.ModelViewSet):
    """
    This viewset automagically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions
    """
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
