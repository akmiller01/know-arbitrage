# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageURL',
            field=models.URLField(help_text=b'Aim for 900x300 resolution', max_length=255, null=True, blank=True),
        ),
    ]
