# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-12 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('des', '0005_auto_20160628_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliance',
            name='default_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='des.OperationTimes'),
        ),
    ]