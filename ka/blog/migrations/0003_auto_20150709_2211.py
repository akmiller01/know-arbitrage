# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150709_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='ticker',
            new_name='symbol',
        ),
    ]
