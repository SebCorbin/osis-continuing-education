# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-09 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0055_auto_20190404_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='awareness_former_students',
            field=models.BooleanField(default=False, verbose_name='By former students'),
        ),
        migrations.AddField(
            model_name='admission',
            name='awareness_friends',
            field=models.BooleanField(default=False, verbose_name='By friends'),
        ),
        migrations.AddField(
            model_name='admission',
            name='awareness_moocs',
            field=models.BooleanField(default=False, verbose_name='By Moocs'),
        ),
        migrations.AddField(
            model_name='admission',
            name='awareness_word_of_mouth',
            field=models.BooleanField(default=False, verbose_name='By word of mouth'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_customized_mail',
            field=models.BooleanField(default=False, verbose_name='By customized mail'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_emailing',
            field=models.BooleanField(default=False, verbose_name='By emailing'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_facebook',
            field=models.BooleanField(default=False, verbose_name='By Facebook'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_formation_website',
            field=models.BooleanField(default=False, verbose_name='By formation website'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_linkedin',
            field=models.BooleanField(default=False, verbose_name='By LinkedIn'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_other',
            field=models.CharField(blank=True, max_length=100, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_press',
            field=models.BooleanField(default=False, verbose_name='By press'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_ucl_website',
            field=models.BooleanField(default=False, verbose_name='By UCL website'),
        ),
    ]
