# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-05 14:47
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0012_auto_20180905_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='admission',
            name='high_school_graduation_year',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='admission',
            name='last_degree_graduation_year',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
