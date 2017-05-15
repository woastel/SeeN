from django.contrib import admin
from .models import (
    Component,
    Component_Type,
    Vendor,
    PCIeCtrl


)
# Register your models here.


admin.site.register(Vendor)
admin.site.register(Component_Type)
admin.site.register(Component)
admin.site.register(PCIeCtrl)
