from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from projects.models import Project
from comments.models import Comment

class Post(models.Model):
    owner = models.ForeignKey(User, related_name='posts')
    project = models.ForeignKey(Project, related_name='posts')

    title = models.CharField(max_length=100)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    comments = generic.GenericRelation(Comment, related_query_name='posts')
