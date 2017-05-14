from django import forms
from .models import Eut, Component_connection
from components.models import Component
from django.contrib.admin.widgets import FilteredSelectMultiple

class Form_Eut_component_connection(forms.ModelForm):
    #   component = forms.ModelMultipleChoiceField(queryset=Component.objects.all(),
    #                                               required=False,
    #                                               widget=FilteredSelectMultiple(
    #                                                   ('tags'),
    #                                                   False,
    #                                                   ))

    class Meta:
        model = Component_connection
        fields = [
            "name",
            "component_count",
            #"eut",
            "component",
            ]




    class Media:
        css = {
            'all':['admin/css/widgets.css',
                   'css/uid-manage-form.css'],
        }

class Form_Eut(forms.ModelForm):

    class Meta:
        model = Eut
        fields = [
            "name",
            "info",
            "user_creator",
            "user_updater",
            "date_creation",
            "date_updateed",
            "system",
            ]

        widgets = {
            'date_creation': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'date_updateed': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            }
