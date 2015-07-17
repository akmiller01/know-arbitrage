# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150717_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageURL',
            field=models.URLField(max_length=255, null=True, blank=True),
        ),
    ]
