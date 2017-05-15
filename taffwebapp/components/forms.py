from django import forms
from .models import (
    Component,
    Component_Type,
    Component_cable_type,
    Component_cable_charackter,
    Component_thermal_charackter,
    Component_mechanik_charackter,
    Component_electronik_charackter,
    Vendor
)

class Form_Component(forms.ModelForm):

    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(),
                                    empty_label="(Nothing)",
                                    required=False)

    information = forms.CharField(required=False,
                                  widget=forms.Textarea)
    #thermal_charakter = forms.ModelChoiceField(
    #                                queryset=Component_thermal_charackter.objects.all(),
    #                                empty_label="(Nothing)",
    #                                required=False)
    #electronic_charakter = forms.ModelChoiceField(
    #                                queryset=Component_electronik_charackter.objects.all(),
    #                                empty_label="(Nothing)",
    #                                required=False)
    #mechanic_charakter = forms.ModelChoiceField(
    #                                queryset=Component_mechanik_charackter.objects.all(),
    #                                empty_label="(Nothing)",
    #                                required=False)
    #cable_charakter = forms.ModelChoiceField(
    #                                queryset=Component_cable_charackter.objects.all(),
    #                                empty_label="(Nothing)",
    #                                required=False)


    class Meta:
        model = Component
        fields = [
            "name",
            "component_type",
            "vendor",

            "thermal_charakter_avalible",
            #"thermal_charakter",
            "electronic_charakter_avalible",
            #"electronic_charakter",
            "mechanic_charakter_avalible",
            #"mechanic_charakter",
            "cable_charakter_avalible",
            #"cable_charakter",

            "date_creation",
            "date_update",
            "user_creator",
            "user_updater",
            "information",
        ]

        widgets = {
            'date_creation': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'date_update': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }

class Form_Component_thermal_charackter(forms.ModelForm):
    max_temperature = forms.DecimalField(required=False)
    required_air_flow = forms.DecimalField(required=False)

    class Meta:
        model = Component_thermal_charackter
        fields = [
            "max_temperature",
            "required_air_flow",
        ]

class Form_Component_electronik_charackter(forms.ModelForm):
    speed = forms.DecimalField(required=False)
    power = forms.DecimalField(required=False)
    class Meta:
        model = Component_electronik_charackter
        fields = [
            "speed",
            "power",
        ]

class Form_Component_mechanik_charackter(forms.ModelForm):
    material = forms.CharField(required=False)
    weight = forms.DecimalField(required=False)
    size_hight = forms.DecimalField(required=False)
    size_length = forms.DecimalField(required=False)
    size_width = forms.DecimalField(required=False)

    class Meta:
        model = Component_mechanik_charackter
        fields = [
            "material",
            "weight",
            "size_hight",
            "size_length",
            "size_width",
        ]

class Form_Component_cable_charackter(forms.ModelForm):


    size_length = forms.DecimalField(required=False)
    cable_type = forms.ModelChoiceField(
                                    queryset=Component_cable_type.objects.all(),
                                    empty_label="(Nothing)",
                                    required=False)
    class Meta:
        model = Component_cable_charackter
        fields = [
            "size_length",
            "cable_type",
        ]
