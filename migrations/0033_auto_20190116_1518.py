# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-16 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0032_file_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
