# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0064_auto_20190508_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continuingeducationtraining',
            name='alternate_notification_email_addresses',
            field=models.TextField(blank=True, default='', help_text='Comma-separated addresses - Leave empty if no address', verbose_name='Alternate notification email addresses'),
        ),
    ]
