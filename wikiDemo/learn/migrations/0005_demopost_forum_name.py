# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_remove_demopost_forum_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='demopost',
            name='forum_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
