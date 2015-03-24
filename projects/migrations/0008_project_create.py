# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150324_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 2, 50, 19, 248362, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
