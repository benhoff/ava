# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20150416_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='idea',
            field=models.ForeignKey(related_name='comments', to='ideas.Idea'),
            preserve_default=True,
        ),
    ]
