# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 11:47
from __future__ import unicode_literals

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
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('createtion_date', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MSDBConnention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('milestoneFinish_date', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Milestone')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SystemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='system',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='system.SystemModel'),
        ),
        migrations.AddField(
            model_name='system',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='system',
            name='owner_co',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cocococococco', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='msdbconnention',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.System'),
        ),
    ]