from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

import collections

from system.models import System as System_System
from components.models import Component



class Eut(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)

    user_creator = models.ForeignKey(User, related_name='%(class)s_requests_created')
    user_updater = models.ForeignKey(User)

    date_creation = models.DateTimeField()
    date_updateed = models.DateTimeField()
    is_connected_to_climaticmeasurement = models.BooleanField(default=False)

    system = models.ForeignKey(System_System, on_delete=models.PROTECT)


    def __str__(self):
        return( str(self.id) + "-" +
                str(self.name) + "-" +
                str(self.system))

    def get_absolute_url(self):
        return reverse('eut:eut_detail', kwargs={'pk': self.pk})



class Component_connection(models.Model):
    info = models.CharField(max_length=100)
    user_creator = models.ForeignKey(User)
    date_creation = models.DateTimeField()

    component_count = models.PositiveIntegerField()

    eut = models.ForeignKey(Eut)
    component = models.ForeignKey(Component)

    def __str__(self):
        return( str(self.id) + "-" +
                str(self.info) + "-" +
                "EUT: " + str(self.eut) + "-" +
                "Comp: " + str(self.component.name))
