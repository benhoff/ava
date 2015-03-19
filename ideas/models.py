from django.db import models
from projects.models import Project
from django.contrib.auth.models import User

class Idea(models.Model):
    owner = models.ForeignKey(User, related_name='ideas') 
    project = models.ForeignKey(Project,related_name='ideas') 

    
    description = models.TextField()
    votes = models.IntegerField()

    created = models.DateTimeField()
    edited = models.DateTimeField(null=True)
    # revisions?
