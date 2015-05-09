from django.db import models
from django.contrib.contenttypes import generic

class Problem(models.Model):
    owner = models.ForeignKey('auth.User', related_name='problems')
    project = models.ForeignKey('project.Project', related_name='problems')
    title = models.CharField(max_length=100)

    description = models.TextField()
    #label

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    comments = generic.GenericRelation('comment.Comment', related_query_name='problems')
    wiki = generic.GenericRelation('wiki.Article', related_query_name='problems')
