# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-18 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0033_auto_20190116_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_category',
            field=models.CharField(choices=[('Document', 'Document'), ('Invoice', 'Invoice'), ('Participant', 'Participant')], default='Document', max_length=20),
        ),
    ]
