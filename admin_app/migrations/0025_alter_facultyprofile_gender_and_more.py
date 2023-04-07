# Generated by Django 4.1.1 on 2022-10-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0024_alter_facultyprofile_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyprofile',
            name='gender',
            field=models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE')], max_length=30),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(choices=[('Female', 'FEMALE'), ('Male', 'MALE')], max_length=30),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='semester',
            field=models.IntegerField(choices=[(4, '4'), (5, '5'), (3, '3'), (1, '1'), (8, '8'), (2, '2'), (7, '7'), (6, '6')], default=1),
        ),
    ]