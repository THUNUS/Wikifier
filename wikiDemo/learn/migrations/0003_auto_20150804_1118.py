# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20150804_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demopost',
            name='forum_name',
            field=models.CharField(max_length=50),
        ),
    ]
