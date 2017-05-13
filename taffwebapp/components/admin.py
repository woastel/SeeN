from django.contrib import admin
from .models import (
    Component,
    Component_Type,
    Component_cable_type,
    Component_cable_charackter,
    Component_thermal_charackter,
    Component_mechanik_charackter,
    Component_electronik_charackter,
    Vendor,


)
# Register your models here.


admin.site.register(Vendor)
admin.site.register(Component_thermal_charackter)
admin.site.register(Component_electronik_charackter)
admin.site.register(Component_mechanik_charackter)
admin.site.register(Component_cable_type)
admin.site.register(Component_cable_charackter)
admin.site.register(Component_Type)
admin.site.register(Component)
