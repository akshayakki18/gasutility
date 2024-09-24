# Generated by Django 5.1.1 on 2024-09-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0007_serviceform_service_request_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceform',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='serviceform',
            name='service_request_type',
            field=models.CharField(choices=[('Installation', 'Installation'), ('Repair', 'Repair'), ('Maintenance', 'Maintenance'), ('Express Shipping', 'Express Shipping'), ('Extended Warranty', 'Extended Warranty')], max_length=100),
        ),
        migrations.AlterField(
            model_name='servicelist',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
