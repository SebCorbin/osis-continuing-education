# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-04 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0046_prospect_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='diploma_produced',
            field=models.BooleanField(default=False, verbose_name='Diploma produced'),
        ),
    ]
