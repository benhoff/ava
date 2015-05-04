from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from comments.models import Comment
from projects.models import Project

class Discussion(models.Model):
    owner = models.ForeignKey(User, related_name='discussions')
    project = models.ForeignKey(Project, related_name='discussions')

    title = models.CharField(max_length=255)

    description = models.TextField()
    comments = generic.GenericRelation(Comment)

    created = models.DateTimeField(auto_now_add=True)
    # null=True?
    edited = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(null=True)

    sticky = models.BooleanField(blank=True, default=False)
    closed = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ['-updated']
        get_latest_by = 'updated'

    #TODO: add in deletion methods
