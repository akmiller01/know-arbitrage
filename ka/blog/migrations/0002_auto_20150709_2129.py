# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='stock',
            field=models.ManyToManyField(related_query_name=b'post', related_name='posts', to='blog.Stock', blank=True),
        ),
    ]
