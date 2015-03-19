# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20150314_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='project',
        ),

        migrations.AddField(
            model_name='idea',
            name='project',
            field=models.ForeignKey(related_name='ideas', to='projects.Project'),
            preserve_default=True,
        ),
    ]
