# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150709_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('subtitle', models.CharField(max_length=255, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('order', models.IntegerField(unique=True)),
                ('content', redactor.fields.RedactorField(verbose_name='Text')),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
