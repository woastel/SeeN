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


# Forms for types this schould only use by the admin
class Form_Vendor(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class Form_Component_Type(forms.ModelForm):
    class Meta:
        model = Component_Type
        fields = '__all__'


# general Forms from the components models
class Form_Chassis(forms.ModelForm):
    class Meta:
        model = Chassis
        # fields = '__all__'
        fields = [  'name',
                    'component_type',
                    'vendor',
                    'material',
                    'size_x',
                    'size_y',
                    'size_z',
                    'model',]

        # exclude = []

class Form_ChassisAddOn(forms.ModelForm):
    class Meta:
        model = ChassisAddOn
        fields = '__all__'

class Form_Motherboard(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = '__all__'

class Form_Cpu(forms.ModelForm):
    class Meta:
        model = Cpu
        fields = '__all__'

class Form_Memory(forms.ModelForm):
    class Meta:
        model = Memory
        fields = '__all__'

class Form_PSU(forms.ModelForm):
    class Meta:
        model = PSU
        fields = '__all__'

class Form_HDD(forms.ModelForm):
    class Meta:
        model = HDD
        fields = '__all__'

class Form_HeatSink(forms.ModelForm):
    class Meta:
        model = HeatSink
        fields = '__all__'

class Form_Fan(forms.ModelForm):
    class Meta:
        model = Fan
        fields = '__all__'

class Form_Cable(forms.ModelForm):
    class Meta:
        model = Cable
        fields = '__all__'

class Form_Pcba(forms.ModelForm):
    class Meta:
        model = Pcba
        fields = '__all__'

class Form_Pcie_Ctrl(forms.ModelForm):
    class Meta:
        model = Pcie_Ctrl
        fields = '__all__'
