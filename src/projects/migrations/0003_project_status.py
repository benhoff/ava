# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default='IDEA', max_length=11, choices=[('IDEA', 'Idea'), ('PROTOTYPE', 'Prototyping'), ('MANUFACTURE', 'Manufacturing'), ('STORE', 'Store')]),
            preserve_default=False,
        ),
    ]
