from django.db import models

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text

from django.contrib.auth.models import User
from ideas.models import Idea

class CommentManager(models.Manager):
    def for_model(self, model):
        """
        QuerySet for all comments for a particualr model 
        (either an instance or a class)
        """
        ct = ContentType.objects.get_for_model(model)
        queryset = self.get_queryset().filter(content_type=ct)
        if isinstance(model, models.Model):
            queryset = queryset.filter(object_pk=force_text(model._get_pk_val()))

        return queryset


class Comment(models.Model):
    # set the manager
    objects = CommentManager()
    
    content_type = models.ForeignKey(ContentType,
                                     verbose_name=_('content type'),
                                     related_name="content_type_set_for%(class)s",
                                     null=True,
                                     blank=True)
    
    object_pk = models.PositiveIntegerField(
            verbose_name=_('related object'),
            null=True)

    content_object = generic.GenericForeignKey(ct_field="content_type", 
                                               fk_field="object_pk")

    owner = models.ForeignKey(User)
    content = models.CharField(max_length=3000)
    #votes = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name=_('comment')
        verbose_name_plural = _('comments')
