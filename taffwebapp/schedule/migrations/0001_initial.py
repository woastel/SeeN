# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 15:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('estimated_days', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Measurement_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('estimated_days', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField()),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.System')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleItem_Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('estimated_end_date', models.DateTimeField()),
                ('certificatio_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Certification_Type')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleItem_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleItem_Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('estimated_end_date', models.DateTimeField()),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('measurement_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Measurement_Type')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Schedule')),
            ],
        ),
    ]
