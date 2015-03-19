# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_auto_20150319_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='edited',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
