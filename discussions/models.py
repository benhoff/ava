from django.db import models
from django.contrib.auth.models import User

from projects.models import Project

class Discussion(models.Model):
    owner = models.ForeignKey(User, related_name='discussions')
    project = models.ForeignKey(Project, related_name='discussions')

    # TODO: Think about the max length variable here. longer?
    title = models.CharField(max_length=100)

    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
