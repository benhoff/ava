# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150314_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner',
            new_name='user',
        ),
    ]
