# Generated by Django 4.2.3 on 2023-09-22 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('health_support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtest',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AddField(
            model_name='labtest',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.patient'),
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_support.diseasecategory'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.patient'),
        ),
    ]
