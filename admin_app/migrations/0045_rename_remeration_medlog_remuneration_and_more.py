# Generated by Django 4.1.1 on 2022-11-10 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0044_medlog_remeration_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medlog',
            old_name='remeration',
            new_name='remuneration',
        ),
        migrations.RenameField(
            model_name='medlog',
            old_name='remeration_date',
            new_name='remuneration_date',
        ),
    ]