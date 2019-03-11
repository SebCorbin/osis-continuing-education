# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-11 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0051_auto_20190308_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='continuing_education.ContinuingEducationTraining', verbose_name='Formation'),
        ),
    ]
