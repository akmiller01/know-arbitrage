# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
