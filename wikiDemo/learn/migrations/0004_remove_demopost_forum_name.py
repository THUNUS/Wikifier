# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_auto_20150804_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demopost',
            name='forum_name',
        ),
    ]
