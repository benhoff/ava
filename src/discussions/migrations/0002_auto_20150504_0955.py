# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discussion',
            options={'get_latest_by': 'updated', 'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='discussion',
            name='closed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discussion',
            name='sticky',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discussion',
            name='updated',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='discussion',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
