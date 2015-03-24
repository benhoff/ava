# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0005_auto_20150319_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='edited',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 2, 50, 31, 552139, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
