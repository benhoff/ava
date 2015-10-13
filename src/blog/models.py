import datetime 

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic

from projects.models import Project
from comments.models import Comment

class Post(models.Model):
    owner = models.ForeignKey(User, related_name='posts')
    project = models.ForeignKey(Project, related_name='posts')

    STATUS_CHOICES=(
            (1, 'Draft'),
            (2, 'Public'),
            )

    title = models.CharField(max_length=255)
    body = models.TextField()
    tease = models.TextField(blank=True, help_text='Concise text suggested. Does not appear in RSS feed')
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=datetime.datetime.now)
    comments = generic.GenericRelation(Comment, related_query_name='posts')

    class Meta:
        ordering = ('-publish',)
        get_latest_by = 'publish'
