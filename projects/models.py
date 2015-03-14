from django.db import models

# Idea generation stage -> Prototyping -> Manufacturing stage -> Store

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    last_updated = models.DateField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='projects')

    STATI = (('IDEA', 'Idea'), 
             ('PROTOTYPE', 'Prototyping'), 
             ('MANUFACTURE', 'Manufacturing'), 
             ('STORE','Store'))

    status = models.CharField(max_length=11, choices=STATI)
    # wiki
    # Code -> Github link? Or something
    # Issues??
    # Ideas
    # forum/discussion
    # 
