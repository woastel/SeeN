from django.db import models
from django.contrib.auth.models import User
from eut.models import Eut


class measurement(models.Model):
    name = models.CharField(max_length=100)
    information = models.TextField(max_length=5000)

    # Dates
    date_creation = models.DateTimeField()
    date_updated = models.DateTimeField()

    # User
    user_creation = models.ForeignKey(User)
    user_updated = models.ForeignKey(User)

    # EUT information
    eut = models.ForeignKey(Eut)

    # measurement result is pass
    # is true or false
    measurement_is_pass = models.BooleanField(default=False)

    # Measurement Type (as text info)
    #  this field will be set by the save methode
    measurement_type = models.CharField(max_length=100)
