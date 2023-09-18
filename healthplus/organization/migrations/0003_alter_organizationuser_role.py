# Generated by Django 4.2.3 on 2023-09-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationuser',
            name='role',
            field=models.CharField(choices=[('OWNER', 'Owner'), ('ADMIN', 'Admin'), ('MANAGER', 'Manager'), ('STAFF', 'Staff')], default='customer', max_length=10),
        ),
    ]
