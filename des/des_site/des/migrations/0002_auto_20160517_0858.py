# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-17 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('des', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='appliance',
            name='house',
        ),
        migrations.RemoveField(
            model_name='house',
            name='street',
        ),
        migrations.AddField(
            model_name='table_link',
            name='appliance_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='des.Appliance'),
        ),
        migrations.AddField(
            model_name='table_link',
            name='house_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='des.House'),
        ),
        migrations.AddField(
            model_name='table_link',
            name='operation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='des.OperationTimes'),
        ),
        migrations.AddField(
            model_name='table_link',
            name='street_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='des.Street'),
        ),
    ]
