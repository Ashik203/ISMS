# Generated by Django 4.1.1 on 2022-10-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0040_rename_rack_no_books_shelf_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(blank=True, choices=[('MATH', 'MATH'), ('PHYSICS', 'PHYSICS'), ('CHEMISTRY', 'CHEMISTRY'), ('HUMANITIES', 'HUMANITIES'), ('ELECTRICAL', 'ELECTRICAL'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'), ('MECHANICAL', 'MECHANIAL'), ('CIVIL', 'CIVIL'), ('INDUSTRIAL', 'INDUSTRIAL'), ('BUSINESS', 'BUSINESS'), ('MAANGEMENT', 'MANAGEMENT')], default=None, max_length=30, null=True),
        ),
    ]