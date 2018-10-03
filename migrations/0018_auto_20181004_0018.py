# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-04 00:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0358_auto_20180921_1059'),
        ('reference', '0020_domain_changed'),
        ('continuing_education', '0017_auto_20180911_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinuingEducationPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('birth_date', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='birth_date')),
                ('birth_location', models.CharField(blank=True, max_length=255, verbose_name='birth_location')),
                ('phone_mobile', models.CharField(blank=True, max_length=30, verbose_name='phone_mobile')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='email')),
                ('high_school_diploma', models.BooleanField(default=False, verbose_name='high_school_diploma')),
                ('high_school_graduation_year', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='high_school_graduation_year')),
                ('last_degree_level', models.CharField(blank=True, max_length=50, verbose_name='last_degree_level')),
                ('last_degree_field', models.CharField(blank=True, max_length=50, verbose_name='last_degree_field')),
                ('last_degree_institution', models.CharField(blank=True, max_length=50, verbose_name='last_degree_institution')),
                ('last_degree_graduation_year', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='last_degree_graduation_year')),
                ('other_educational_background', models.TextField(blank=True, verbose_name='other_educational_background')),
                ('professional_status', models.CharField(blank=True, choices=[('EMPLOYEE', 'employee'), ('SELF_EMPLOYED', 'self_employed'), ('JOB_SEEKER', 'job_seeker'), ('PUBLIC_SERVANT', 'public_servant'), ('OTHER', 'other')], max_length=50, verbose_name='professional_status')),
                ('current_occupation', models.CharField(blank=True, max_length=50, verbose_name='current_occupation')),
                ('current_employer', models.CharField(blank=True, max_length=50, verbose_name='current_employer')),
                ('activity_sector', models.CharField(blank=True, choices=[('PRIVATE', 'private'), ('PUBLIC', 'public'), ('ASSOCIATIVE', 'associative'), ('HEALTH', 'health'), ('OTHER', 'other')], max_length=50, verbose_name='activity_sector')),
                ('past_professional_activities', models.TextField(blank=True, verbose_name='past_professional_activities')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='birth_country',
        ),
        migrations.RemoveField(
            model_name='person',
            name='citizenship',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='person',
        ),
        migrations.AddField(
            model_name='address',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='admission',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_country', to='reference.Country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='address',
            name='location',
            field=models.CharField(blank=True, max_length=255, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, verbose_name='postal_code'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='assessment_presented',
            field=models.BooleanField(default=False, verbose_name='assessment_presented'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='assessment_succeeded',
            field=models.BooleanField(default=False, verbose_name='assessment_succeeded'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_customized_mail',
            field=models.BooleanField(default=False, verbose_name='awareness_customized_mail'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_emailing',
            field=models.BooleanField(default=False, verbose_name='awareness_emailing'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_facebook',
            field=models.BooleanField(default=False, verbose_name='awareness_facebook'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_formation_website',
            field=models.BooleanField(default=False, verbose_name='awareness_formation_website'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_linkedin',
            field=models.BooleanField(default=False, verbose_name='awareness_linkedin'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_press',
            field=models.BooleanField(default=False, verbose_name='awareness_press'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='awareness_ucl_website',
            field=models.BooleanField(default=False, verbose_name='awareness_ucl_website'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='continuing_education.Address', verbose_name='billing_address'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='children_number',
            field=models.SmallIntegerField(blank=True, default=0, verbose_name='children_number'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='company_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='company_number'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='formation',
            field=models.CharField(default='-', max_length=50, verbose_name='formation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admission',
            name='formation_spreading',
            field=models.BooleanField(default=False, verbose_name='formation_spreading'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='head_office_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='head_office_name'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='id_card_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='id_card_number'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('SINGLE', 'single'), ('MARRIED', 'married'), ('WIDOWED', 'widowed'), ('DIVORCED', 'divorced'), ('SEPARATED', 'separated'), ('LEGAL_COHABITANT', 'legal_cohabitant')], max_length=255, verbose_name='marital_status'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='motivation',
            field=models.TextField(blank=True, verbose_name='motivation'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='national_registry_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='national_registry_number'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='noma',
            field=models.CharField(blank=True, max_length=255, verbose_name='noma'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='passport_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='passport_number'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='payment_complete',
            field=models.BooleanField(default=False, verbose_name='payment_complete'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='previous_noma',
            field=models.CharField(blank=True, max_length=255, verbose_name='previous_noma'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='previous_ucl_registration',
            field=models.BooleanField(default=False, verbose_name='previous_ucl_registration'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='prior_experience_validation',
            field=models.BooleanField(default=False, verbose_name='prior_experience_validation'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='professional_impact',
            field=models.TextField(blank=True, verbose_name='professional_impact'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='registration_complete',
            field=models.BooleanField(default=False, verbose_name='registration_complete'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='registration_type',
            field=models.CharField(blank=True, choices=[('PRIVATE', 'private'), ('PROFESSIONAL', 'professional')], max_length=50, verbose_name='registration_type'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='residence_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='residence_address', to='continuing_education.Address', verbose_name='residence_address'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='residence_phone',
            field=models.CharField(blank=True, max_length=30, verbose_name='residence_phone'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='sessions',
            field=models.CharField(blank=True, max_length=255, verbose_name='sessions'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='spouse_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='spouse_name'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='state',
            field=models.CharField(blank=True, choices=[('accepted', 'accepted'), ('rejected', 'rejected'), ('waiting', 'waiting')], max_length=50, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='use_address_for_billing',
            field=models.BooleanField(default=False, verbose_name='use_address_for_billing'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='use_address_for_post',
            field=models.BooleanField(default=False, verbose_name='use_address_for_post'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='vat_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='vat_number'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='continuingeducationperson',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='continuing_education.Address', verbose_name='address'),
        ),
        migrations.AddField(
            model_name='continuingeducationperson',
            name='birth_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='birth_country', to='reference.Country', verbose_name='birth_country'),
        ),
        migrations.AddField(
            model_name='continuingeducationperson',
            name='citizenship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='citizenship', to='reference.Country', verbose_name='citizenship'),
        ),
        migrations.AddField(
            model_name='continuingeducationperson',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.Person'),
        ),
        migrations.AddField(
            model_name='admission',
            name='person_information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='continuing_education.ContinuingEducationPerson', verbose_name='person_information'),
        ),
    ]
