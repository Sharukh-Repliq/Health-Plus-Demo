# Generated by Django 4.2.3 on 2023-09-22 06:01

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('health_support', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(choices=[('PENDIN', 'Pending'), ('IN_TRANSIT', 'In_Transit'), ('DELIVERED', 'Delivered'), ('FAILED', 'Failed'), ('COMPLETED', 'Completed')], default='Pending', max_length=20)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=255)),
                ('delivery_address', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('quantity', models.PositiveIntegerField()),
                ('labtest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_support.labtest')),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_support.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_management.order')),
            ],
        ),
    ]
