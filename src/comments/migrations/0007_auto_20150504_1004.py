# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0006_auto_20150425_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Edited by', null=True, related_name='comment_edits'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='edited',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comments'),
            preserve_default=True,
        ),
    ]
