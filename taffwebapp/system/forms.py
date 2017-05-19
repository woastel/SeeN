from django import forms
from .models import (
    System,
    SystemModel,
    Milestone,
    MSDBConnention )


class Create_System_Form(forms.ModelForm):
    class Meta:
        model = System
        fields = [
            "name",
            "info",
            "model",
            "owner",
            "owner_co",
        ]

class Create_SystemModel_Form(forms.ModelForm):
    class Meta:
        model = SystemModel
        fields = [
            "name"
        ]

class Create_Milestone_Form(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = [
            "name",
            "info",
            "creator",
            "createtion_date",
        ]

        # Change the withget -attrs class- to activate the datetime input (JavaScript)
        widgets = {
            'createtion_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }

class Create_MSDBConnention_Form(forms.ModelForm):
    class Meta:
        model = MSDBConnention
        fields = [
            "system",
            "milestone",
            "creator",
            "creation_date",
            "milestoneFinish_date",
        ]

        # Change the withget -attrs class- to activate the datetime input (JavaScript)
        widgets = {
            'creation_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
            'milestoneFinish_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }

class Create_MSDBConnention_Form2(forms.ModelForm):
    class Meta:
        model = MSDBConnention
        fields = [
            "milestone",
            "milestoneFinish_date",
        ]

        # Change the withget -attrs class- to activate the datetime input (JavaScript)
        widgets = {
            'milestoneFinish_date': forms.DateTimeInput(
                                    attrs={'class':'datetime-input'}),
        }
