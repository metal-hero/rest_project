# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 26, 11, 33, 53, 627944, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
