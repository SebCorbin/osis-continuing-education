# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-01 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0044_admission_registration_file_received'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Name')),
                ('first_name', models.CharField(blank=True, max_length=250, verbose_name='First name')),
                ('postal_code', models.CharField(blank=True, max_length=250, verbose_name='Postal code')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=30, verbose_name='Phone number')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
