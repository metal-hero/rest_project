# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20150305_0512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titile',
            new_name='title',
        ),
    ]
