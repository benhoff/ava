from django.db import models
from projects.models import Project
from django.contrib.auth.models import User

class Idea(models.Model):
    owner = models.ForeignKey(User, related_name='ideas') 
    project = models.ManyToManyField(Project)
    
    description = models.TextField()
    votes = models.IntegerField()

    created = models.DateTimeField()
    edited = models.DateTimeField()
    # revisions?
