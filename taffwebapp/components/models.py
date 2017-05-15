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

class ComponentMechanicalCharackter(Component):
    length = models.IntegerField()
    width = models.IntegerField()
    high = models.IntegerField()

class ComponentThermalChararckter(ComponentMechanicalCharackter):
    maxthermperature = models.IntegerField()
    airflowminimum = models.IntegerField()

class PCIeCtrl(ComponentThermalChararckter):
    test = models.IntegerField()
