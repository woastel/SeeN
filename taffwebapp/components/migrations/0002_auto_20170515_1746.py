# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Component_ThermalCharackter',
            new_name='Component_ThermalCharacter',
        ),
        migrations.RenameField(
            model_name='component_thermalcharacter',
            old_name='thermalCharackter_id',
            new_name='thermalCharacter_id',
        ),
        migrations.RenameField(
            model_name='pciectrl',
            old_name='component_thermalcharackter_ptr',
            new_name='component_thermalcharacter_ptr',
        ),
        migrations.AlterField(
            model_name='pciectrl',
            name='component_thermalcharacter_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='components.Component_ThermalCharackter', to_field='thermalCharacter_id'),
        ),
    ]
