# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='max_time',
            field=models.TimeField(verbose_name=b'maximum time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='min_time',
            field=models.TimeField(verbose_name=b'minimum time', blank=True),
            preserve_default=True,
        ),
    ]
