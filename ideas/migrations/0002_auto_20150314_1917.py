# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
