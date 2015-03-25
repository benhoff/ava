from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import ContentType, generic

from votes.managers import VoteManager

SCORES = (
        (u'+1', +1),
        (u'-1', -1)
)


class Vote(models.Model):
    owner = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = generic.GenericForeignKey('content_type', 'object_id')
    vote = models.SmallIntegerField(choices=SCORES)

    objects = VoteManager()

    class Meta:
        db_table = 'votes'
        unique_together = (('user', 'content_type', 'object_id'))

    def __unicode__(self):
        return u'{}: {} on {}'.format(self.user, self.vote, self.object)

    def is_upvote(self):
        return self.vote == 1

    def is_downvote(self):
        return self.vote == -1
