# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-09-24 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0069_continuingeducationtraining_additional_information_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='comment',
            field=models.TextField(blank=True, null=True, max_length=500, verbose_name='Comment'),
        ),
    ]