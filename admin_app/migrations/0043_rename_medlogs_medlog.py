# Generated by Django 4.1.1 on 2022-11-10 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0042_medlogs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedLogs',
            new_name='MedLog',
        ),
    ]