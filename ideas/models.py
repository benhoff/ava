from django.db import models
from projects.models import Project
from django.contrib.auth.models import User

class Idea(models.Model):
    owner = models.ForeignKey(User, related_name='ideas') 
    project = models.ForeignKey(Project,related_name='ideas') 

    
    description = models.TextField()
    votes = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    # revisions?
