from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.contrib.contenttypes import generic
from datetime import datetime

class Room(models.Model):
    # to what kind of object is this related 
    content_type = models.ForeignKey(models.ContentType)   

    # to which instace of the aforementioned object is this related 
    object_id = models.PositiveIntegerField()        

    # use both up, USE THIS WHEN INSTANCING THE MODEL
    content_object = generic.GenericForeignKey('content_type','object_id')
    created = models.DateTimeField(default=datetime.now())
    comment = models.TextField(blank=True, null=True)

MESSAGE_TYPE_CHOICES = (
        ('s', 'system'),
        ('a', 'action'),
        ('m', 'message'),
        ('j', 'join'),
        ('l', 'leave'),
        ('n', 'notification')
)

class Message(models.Model):
    """
    A message that belong to a chat room
    """
    author = models.ForeignKey(User, related_name='author', blank=True, null=True)
    message = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        if self.type == 's':
            return u'SYSTEM: %s' % self.message        
        elif self.type == 'n':                                    
            return u'NOTIFICATION: %s' % self.message        
        elif self.type == 'j':
            return 'JOIN: %s' % self.author        
        elif self.type == 'l':
            return 'LEAVE: %s' % self.author        
        elif self.type == 'a': 
            return 'ACTION: %s > %s' % (self.author, self.message)
        return self.message
