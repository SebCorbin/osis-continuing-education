# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-17 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0022_remove_state_constraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='state',
            field=models.CharField(blank=True, choices=[('accepted', 'accepted'), ('rejected', 'rejected'), ('waiting', 'waiting'), ('draft', 'draft'), ('submitted', 'submitted')], max_length=50, null=True, verbose_name='state'),
        ),
    ]
