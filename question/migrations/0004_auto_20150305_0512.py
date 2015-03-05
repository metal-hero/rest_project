# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20150304_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=150)),
                ('titile', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=1500)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('upd_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_public', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='question.Post'),
            preserve_default=True,
        ),
    ]
