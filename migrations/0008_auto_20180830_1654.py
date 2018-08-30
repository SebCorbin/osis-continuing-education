# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-30 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0007_auto_20180830_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='customized_mail',
            new_name='awareness_customized_mail',
        ),
        migrations.RenameField(
            model_name='admission',
            old_name='emailing',
            new_name='awareness_emailing',
        ),
        migrations.RenameField(
            model_name='admission',
            old_name='facebook',
            new_name='awareness_facebook',
        ),
        migrations.RenameField(
            model_name='admission',
            old_name='formation_website',
            new_name='awareness_formation_website',
        ),
        migrations.RenameField(
            model_name='admission',
            old_name='linkedin',
            new_name='awareness_linkedin',
        ),
        migrations.RenameField(
            model_name='admission',
            old_name='press',
            new_name='awareness_press',
        ),
        migrations.RenameField(
            model_name='admission',
            old_name='ucl_website',
            new_name='awareness_ucl_website',
        ),
    ]