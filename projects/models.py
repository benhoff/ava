from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    last_updated = models.DateField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='projects')
