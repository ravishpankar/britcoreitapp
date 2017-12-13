# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-13 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('riskname', models.CharField(max_length=50)),
                ('riskid', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='RiskTypeAttribute',
            fields=[
                ('riskattrid', models.AutoField(primary_key=True, serialize=False)),
                ('riskattrname', models.CharField(max_length=50)),
                ('riskattrtype', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('risktype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metarisk.RiskType')),
            ],
        ),
        migrations.CreateModel(
            name='RiskTypeAttributeEnumEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riskenumentryname', models.CharField(max_length=10)),
                ('riskenumentryvalue', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('riskattr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metarisk.RiskTypeAttribute')),
            ],
        ),
    ]