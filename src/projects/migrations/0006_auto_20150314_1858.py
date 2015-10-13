# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20150314_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='child_projects',
            field=models.ManyToManyField(related_name='child', to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='parent_projects',
            field=models.ManyToManyField(related_name='parent', to='projects.Project'),
            preserve_default=True,
        ),
    ]
