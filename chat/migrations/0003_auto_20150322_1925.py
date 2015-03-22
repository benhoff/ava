# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 22, 19, 25, 13, 741862)),
            preserve_default=True,
        ),
    ]
