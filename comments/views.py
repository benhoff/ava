from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import viewsets

class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automagically provides 'list', 'create', 'retieve', 'update', and     'destroy' actions
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
