# Generated by Django 2.1.1 on 2018-09-18 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bw3backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orga_units',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bw3backend.orga_location'),
        ),
        migrations.AlterField(
            model_name='orga_units',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bw3backend.orga_units'),
        ),
        migrations.AlterField(
            model_name='orga_units',
            name='vehicals',
            field=models.ManyToManyField(blank=True, null=True, to='bw3backend.orga_vehical'),
        ),
    ]
