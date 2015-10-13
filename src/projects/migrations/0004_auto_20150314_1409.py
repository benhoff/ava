# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.SlugField(max_length=30),
            preserve_default=True,
        ),
    ]
