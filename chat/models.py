from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.contrib.contenttypes import generic
from datetime import datetime

# https://pythonhaven.wordpress.com/2009/07/13/django-powered-ajax-chat-%E2%80%93-part-2/

class RoomManager(models.Manager):
    def create(self, object):
        """
        creates a new chat room and registers it to the calling object
        """
        r = self.model(content_object=object)
        r.save()
        return r

    def get_for_object(self, object):
        """
        Try to get a room related to the object passed
        """
        return self.get(content_type=ContentType.objects.get_for_model(object), object_id = object.pk)

    def get_or_create(self, object):
        """
        save us the hassle of validating the return value
        """
        try:
            return self.get_for_object(object)
        except:
            return self.create(object)


class Room(models.Model):
    # to what kind of object is this related 
    content_type = models.ForeignKey(ContentType)   

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
