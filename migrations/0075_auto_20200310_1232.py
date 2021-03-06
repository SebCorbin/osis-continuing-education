# Generated by Django 2.2.5 on 2020-03-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continuing_education', '0074_admission_academic_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='ucl_registration_complete',
            field=models.CharField(blank=True, choices=[('Initial state', 'Initial state'), ('Sended', 'Sended'), ('Registered', 'Registered'), ('On demand', 'On demand'), ('Rejected', 'Rejected')], default='Initial state', max_length=50, verbose_name='UCLouvain registration complete'),
        ),
    ]
