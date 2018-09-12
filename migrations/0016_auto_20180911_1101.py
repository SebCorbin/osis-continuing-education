# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-11 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0015_admission_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='billing_city',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='billing_country',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='billing_location',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='billing_postal_code',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='residence_city',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='residence_country',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='residence_location',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='residence_postal_code',
        ),
        migrations.AddField(
            model_name='admission',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='continuing_education.PersonAddress'),
        ),
        migrations.AddField(
            model_name='admission',
            name='residence_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='residence_address', to='continuing_education.PersonAddress'),
        ),
    ]