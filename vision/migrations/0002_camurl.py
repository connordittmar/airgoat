# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vision', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CamUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camurl', models.TextField(blank=True, default='http://169.254.171.248/mjpg/video.mjpg')),
            ],
        ),
    ]
