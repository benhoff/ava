from django.db import models
from django.contrib.contenttypes import generic

# TODO: Think about how to make a separate table (maybe?) for each project ideas

class Idea(models.Model):
    owner = models.ForeignKey('auth.User', related_name='ideas') 
    project = models.ForeignKey('project.Project',related_name='ideas') 
    title = models.CharField(max_length=100)
    
    description = models.TextField()
    votes = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    comments = generic.GenericRelation('comment.Comment', 
                                       related_query_name='ideas') 

    wiki = generic.GenericRelation('wiki.Article',
                                   related_query_name='ideas')
    # revisions?
