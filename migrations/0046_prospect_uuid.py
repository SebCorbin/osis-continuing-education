# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-01 14:22
from __future__ import unicode_literals

import uuid

import django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0045_prospect'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospect',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AddField(
            model_name='prospect',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    to='base.EducationGroupYear', verbose_name='Formation'),
        ),
    ]
