from django import forms
from .models import (
    Vendor,
    Component_Type,
    Component,
    Component_Character_Thermal,
    Component_Character_Mechanical,
    Component_Character_Electrical_Power,

    Chassis,
    ChassisAddOn,
    Motherboard,
    Cpu,
    Memory,
    PSU,
    HDD,
    HeatSink,
    Fan,
    Cable,
    Pcba,
    Pcie_Ctrl
)


class Form_Chassis(forms.ModelForm):

    class Meta:
        model = Chassis
        fields = '__all__'
