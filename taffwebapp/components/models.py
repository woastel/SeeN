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

class Component_ThermalCharacter(models.Model):
    thermalCharacter_id = models.AutoField(primary_key=True)
    maxtemp = models.IntegerField()

class Component_MechanicalCharacter(models.Model):
    material = models.CharField()
    size_x = models.DecimalField(max_digits=10, decimal_places=2)
    size_y = models.DecimalField(max_digits=10, decimal_places=2)
    size_z = models.DecimalField(max_digits=10, decimal_places=2)

class Component_ElectricalCharacter(models.Model):
    power = models.DecimalField(max_digits=10, decimal_places=2)

# Component specifit characters



# Die eigentlichen Components
class PCIeCtrl(Component, Component_ThermalCharacter):
    test = models.IntegerField()
