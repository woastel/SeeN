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

    # Character avalible
    character_mechanical_avalible = models.BooleanField(default=False)
    character_electrical_avalible = models.BooleanField(default=False)
    character_thermal_avalible = models.BooleanField(default=False)

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
    airflow_min = models.IntegerField()

# Component Tables Specified
class Chassis       (Component, Component_Character_Mechanical):
    model = models.IntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class ChassisAddOn  (Component, Component_Character_Mechanical):
    model = models.IntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class Motherboard   (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    pcie_slot_count = models.PositiveIntegerField()
    cpu_slot_count = models.PositiveIntegerField()
    psu_slot_count = models.PositiveIntegerField()
    memory_slot_count = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class Cpu           (Component, Component_Character_Electrical_Power, Component_Character_Thermal):
    cores = models.IntegerField()
    TDP = models.FloatField()
    frequency = models.FloatField()
    klasse = models.FloatField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = False
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class Memory        (Component, Component_Character_Electrical_Power, Component_Character_Thermal):
    capacity = models.IntegerField()
    ddr_version = models.CharField()
    speed_frequency = models.FloatField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = False
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class PSU           (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    power_class = models.CharField()
    formfactor = models.CharField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class HDD           (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    capacity = models.PositiveIntegerField()
    technology = models.CharField(lenght=100)

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class HeatSink      (Component, Component_Character_Mechanical):
    technology = models.CharField(lenght=100)

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class Fan           (Component, Component_Character_Mechanical):
    maximum_rpm = models.IntegerField()
    maximum_airflow = models.IntegerField()
    maximum_pressure = models.IntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class Cable         (Component, Component_Character_Mechanical):
    cable_type = models.CharField(length=100)
    lenght = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class Pcba          (Component, Component_Character_Mechanical):
    pcba_type = models.CharField(length=100)

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = False
        self.character_thermal_avalible = False
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)

class Pcie_Ctrl     (Component, Component_Character_Mechanical, Component_Character_Electrical_Power, Component_Character_Thermal):
    pcie_spec = models.IntegerField()
    pcie_lanes_electrical = models.IntegerField()
    pcie_lanes_mechanical = models.IntegerField()
    pcie_ctrl_type = models.IntegerField()

    def save(self, *args, **kwargs):
        # Set the Character Bools
        self.character_mechanical_avalible = True
        self.character_electrical_avalible = True
        self.character_thermal_avalible = True
        # Call the Super Methode
        super(Chassis, self).save(*args, **kwargs)
