from projects.models import Project
from projects.serializers import ProjectSerializer, UserSerializer
from projects.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automagically provides 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        project = self.get_object()
        return Response(project.description)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
