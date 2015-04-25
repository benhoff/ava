from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_extensions.permissions import IsOwnerOrReadOnly
from blog.models import Post
from blog.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset is nested under projects and provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # TODO: Implement more permissions here
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def list(self, request, project_pk=None):
        posts = self.queryset.filter(project_id=project_pk)
        serializer = PostSerializer(posts,
                                    many=True,
                                    context={'request':request})

        return Response(serializer.data)

    def perform_create(self, serialzier):
        serializer.save(owner=self.request.user)
