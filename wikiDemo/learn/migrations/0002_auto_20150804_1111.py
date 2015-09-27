# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Struct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('code', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='demopost',
            name='forum_name',
            field=models.CharField(default='ml', max_length=150),
            preserve_default=False,
        ),
    ]
