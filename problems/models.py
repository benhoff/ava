from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic

from projects.models import Project
from comments.models import Comment

class Problem(models.Model):
    owner = models.ForeignKey(User, related_name='problems')
    project = models.ForeignKey(Project, related_name='problems')
    title = models.CharField(max_length=100)

    description = models.TextField()
    #label

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    comments = generic.GenericRelation(Comment, related_query_name='problems')
