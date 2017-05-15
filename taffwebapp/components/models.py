from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(str(self.name))

class Component_Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(str(self.name))

# Component Table
class Component(models.Model):
    component_id = models.AutoField(primary_key=True)


    name = models.CharField(max_length=100)
    component_type = models.ForeignKey(Component_Type)
    vendor = models.ForeignKey(Vendor, models.SET_NULL, null=True)

    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()
    user_creator = models.ForeignKey(User)
    user_updater= models.ForeignKey(User, related_name='%(class)s_requests_created')
    information = models.TextField(max_length=5000)

    def __str__(self):
        return(str(self.component_type.name) + " - " + str(self.name))

# Component Character Tables

class Component_Character_Mechanical(models.Model):
    character_mechaical_id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=100)
    size_x = models.DecimalField(max_digits=10, decimal_places=2)
    size_y = models.DecimalField(max_digits=10, decimal_places=2)
    size_z = models.DecimalField(max_digits=10, decimal_places=2)

class Component_Character_Electrical_Power(models.Model):
    character_electrical_id = models.AutoField(primary_key=True)
    power_max = models.DecimalField(max_digits=10, decimal_places=2)
    power_typical = models.DecimalField(max_digits=10, decimal_places=2)
    power_minimal = models.DecimalField(max_digits=10, decimal_places=2)

class Component_Character_Thermal(models.Model):
    character_thermal_id = models.AutoField(primary_key=True)
    temperature_max = models.IntegerField()
    airflow_max = models.IntegerField()

# Component Tables Specified

class Chassis       (Component, Component_Character_Mechanical):
    model = models.IntegerField()

class ChassisAddOn  (Component, Component_Character_Mechanical):
    model = models.IntegerField()

class Motherboard   (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    pcie_slot_count = models.IntegerField()
    cpu_slot_count = models.IntegerField()
    psu_slot_count = models.IntegerField()
    memory_slot_count = models.IntegerField()

class Cpu           (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    cores = models.IntegerField()
    TDP = models.IntegerField()
    frequency = models.IntegerField()
    klasse = models.IntegerField()

class Memory        (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    capacity = models.IntegerField()
    ddr_version = models.IntegerField()
    speed_frequency = models.IntegerField()

class PSU           (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    power_class = models.IntegerField()
    formfactor = models.IntegerField()

class HDD           (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    capacity = models.IntegerField()
    technology = models.IntegerField()

class HeatSink      (Component, Component_Character_Mechanical):
    technology = models.IntegerField()

class Fan           (Component, Component_Character_Mechanical):
    maximum_rpm = models.IntegerField()
    maximum_airflow = models.IntegerField()
    maximum_pressure = models.IntegerField()

class Cable         (Component, Component_Character_Mechanical):
    cable_type = models.IntegerField()
    lenght = models.IntegerField()

class Pcba          (Component, Component_Character_Mechanical):
    pcba_type = models.IntegerField()

class Pcie_Ctrl     (Component, Component_Character_Mechanical):
    pcie_spec = models.IntegerField()
    pcie_lanes_electrical = models.IntegerField()
    pcie_lanes_mechanical = models.IntegerField()
    pcie_ctrl_type = models.IntegerField()
