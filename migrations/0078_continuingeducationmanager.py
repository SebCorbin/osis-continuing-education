# Generated by Django 2.2.10 on 2020-03-18 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0508_auto_20200318_1024'),
        ('continuing_education', '0077_auto_20200316_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinuingEducationManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Person')),
            ],
            options={
                'verbose_name': 'Continuing Education Manager',
                'verbose_name_plural': 'Continuing Education Managers',
            },
        ),
    ]
