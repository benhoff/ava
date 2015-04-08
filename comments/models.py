from django.db import models
from django.contrib.auth.models import User
from ideas.models import Idea

class Comment(models.Model):
    owner = models.ForeignKey(User)
    content = models.CharField(max_length=500)
    idea = models.ForeignKey(Idea)
    #votes = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
