# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'publish', 'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=2, choices=[(1, 'Draft'), (2, 'Public')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='tease',
            field=models.TextField(help_text='Concise text suggested. Does not appear in RSS feed', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
