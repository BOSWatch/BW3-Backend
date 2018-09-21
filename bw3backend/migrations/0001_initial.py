# Generated by Django 2.1.1 on 2018-09-18 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='client_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.client')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workload', models.CharField(max_length=255)),
                ('direction', models.BooleanField()),
                ('callid', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='dataincoming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cliententrytime', models.DateTimeField()),
                ('workload', models.CharField(max_length=255)),
                ('direction', models.BooleanField()),
                ('callid', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.client')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='globalconfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='helper_datatype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='orga_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('addr_street', models.CharField(max_length=30)),
                ('addr_nr', models.CharField(max_length=4)),
                ('addr_plz', models.TextField(max_length=100)),
                ('addr_city', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='orga_units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=255)),
                ('optaname', models.TextField(max_length=75)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.orga_location')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.orga_units')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='orga_vehical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('optaname', models.CharField(max_length=30)),
                ('numberplate', models.TextField(max_length=100)),
                ('fmskennung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.data')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.orga_location')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('version', models.DecimalField(decimal_places=2, max_digits=2)),
                ('builddate', models.DateField()),
                ('creator', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='plugin_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=255)),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.plugin')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='plugininstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('set_active', models.BooleanField()),
                ('set_callbychild', models.BooleanField()),
                ('set_calldirect', models.BooleanField()),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.plugin')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='plugininstance_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=255)),
                ('plugininstance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.plugininstance')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AddField(
            model_name='orga_units',
            name='vehicals',
            field=models.ManyToManyField(to='bw3backend.orga_vehical'),
        ),
        migrations.AddField(
            model_name='dataincoming',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.helper_datatype'),
        ),
        migrations.AddField(
            model_name='data',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bw3backend.helper_datatype'),
        ),
    ]
