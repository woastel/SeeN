# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0007_auto_20170512_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component_cable_charackter',
            name='size_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]