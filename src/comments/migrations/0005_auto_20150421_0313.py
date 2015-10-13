# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('comments', '0004_auto_20150416_0241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'comments', 'verbose_name': 'comment'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='idea',
        ),
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(related_name='content_type_set_forcomment', to='contenttypes.ContentType', blank=True, null=True, verbose_name='content type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='object_pk',
            field=models.PositiveIntegerField(null=True, verbose_name='related object'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=3000),
            preserve_default=True,
        ),
    ]
