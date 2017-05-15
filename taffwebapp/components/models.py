from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(str(self.name))

class Component_thermal_charackter(models.Model):
    max_temperature = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    required_air_flow = models.DecimalField(blank=True, null=True,max_digits=6, decimal_places=2)

class Component_electronik_charackter(models.Model):
    speed = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    power = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)

class Component_mechanik_charackter(models.Model):
    material = models.CharField(blank=True, null=True, max_length=500)
    weight = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    size_hight = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    size_length = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    size_width = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)

class Component_cable_type(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return(str(self.name))

class Component_cable_charackter(models.Model):
    size_length = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    cable_type = models.ForeignKey(Component_cable_type)

class Component_pcie_ctrl_charackter(models.Model):
    pcie_ctrl_slot_mechanical = models.CharField(max_length=100)

class Component_Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return(str(self.name))

class Component(models.Model):
    name = models.CharField(max_length=100)
    component_type = models.ForeignKey(Component_Type)
    vendor = models.ForeignKey(Vendor, models.SET_NULL, null=True)

    thermal_charakter_avalible = models.BooleanField(default=True)
    thermal_charakter = models.ForeignKey(Component_thermal_charackter, models.SET_NULL, null=True)
    electronic_charakter_avalible = models.BooleanField(default=True)
    electronic_charakter = models.ForeignKey(Component_electronik_charackter, models.SET_NULL, null=True)
    mechanic_charakter_avalible = models.BooleanField(default=True)
    mechanic_charakter = models.ForeignKey(Component_mechanik_charackter, models.SET_NULL, null=True)
    cable_charakter_avalible = models.BooleanField(default=True)
    cable_charakter = models.ForeignKey(Component_cable_charackter, models.SET_NULL, null=True)

    date_creation = models.DateTimeField()
    date_update = models.DateTimeField()
    user_creator = models.ForeignKey(User)
    user_updater= models.ForeignKey(User, related_name='%(class)s_requests_created')
    information = models.TextField(max_length=5000)


    def __str__(self):
        return(str(self.component_type.name) + " - " + str(self.name))
