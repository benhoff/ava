# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_auto_20150421_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='object_pk',
            new_name='object_id',
        ),
    ]
