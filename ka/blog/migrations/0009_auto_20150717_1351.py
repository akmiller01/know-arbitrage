# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='author_ip',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
