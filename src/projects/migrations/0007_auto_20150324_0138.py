# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20150314_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='owner',
        ),
    ]
