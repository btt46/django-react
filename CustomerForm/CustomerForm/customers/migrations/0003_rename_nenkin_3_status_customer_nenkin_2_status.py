# Generated by Django 3.2 on 2021-04-07 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='nenkin_3_status',
            new_name='nenkin_2_status',
        ),
    ]
