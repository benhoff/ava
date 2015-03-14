# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_auto_20150314_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='owner',
            field=models.ForeignKey(related_name='ideas', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
