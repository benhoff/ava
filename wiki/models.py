from django.db import models

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class ArticleRevision(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    revision_number = models.IntegerField(editable=False)
    owner = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.SET_NULL)
    edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    previous_revision = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    locked = models.BooleanField(default=False)

# TODO: add in comment like generic types.
class Article(models.Model):
    current_revision = models.OneToOneField('ArticleRevision', verbose_name='current revision',
                                            blank=True, null=True, related_name='current_set')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, blank=True, 
                              null=True, related_name='owned_articles', 
                              on_delete=models.SET_NULL)

    # Group? group read(boolean field)? group write (boolean field)?
