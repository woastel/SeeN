from django import forms
from .models import Eut

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
