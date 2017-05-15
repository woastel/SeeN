from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from datetime import datetime
from .models import (Component)


#
# Main View
#-------------------------
@method_decorator(login_required, name='dispatch')
class MainView(View):
    templateName = 'components/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        usernameRequest = self.request.user.username

        return render(request, self.templateName, context)

#
# Create Types + Vendor
#-------------------------
@method_decorator(login_required, name='dispatch')
class Create_Component_Type_View(View):
    form_class = forms.Form_Component_Type
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Component Type"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_Vendor_View(View):
    form_class = forms.Form_Vendor
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Vendor"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

#
# Create Components
#-------------------------
@method_decorator(login_required, name='dispatch')
class Create_Chassis_View(View):
    form_class = forms.Form_Chassis
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Chassis"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_ChassisAddOn_View(View):
    form_class = forms.Form_ChassisAddOn
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Chassis Add On"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_Motherboard_View(View):
    form_class = forms.Form_Motherboard
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Motherboard"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_CPU_View(View):
    form_class = forms.Form_Cpu
    templateName = 'components/component_create.html'
    panel_titel = "Create a new CPU"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_Memory_View(View):
    form_class = forms.Form_Memory
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Memory"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_PSU_View(View):
    form_class = forms.Form_PSU
    templateName = 'components/component_create.html'
    panel_titel = "Create a new PSU"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_HDD_View(View):
    form_class = forms.Form_HDD
    templateName = 'components/component_create.html'
    panel_titel = "Create a new HDD"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_HeatSink_View(View):
    form_class = forms.Form_HeatSink
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Heatsink"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_Fan_View(View):
    form_class = forms.Form_Fan
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Fan"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_Cable_View(View):
    form_class = forms.Form_Cable
    templateName = 'components/component_create.html'
    panel_titel = "Create a new Cable"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_Pcba_View(View):
    form_class = forms.Form_Pcba
    templateName = 'components/component_create.html'
    panel_titel = "Create a new PCBA"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Create_PcieCtrl_View(View):
    form_class = forms.Form_Pcie_Ctrl
    templateName = 'components/component_create.html'
    panel_titel = "Create a new PCIe Ctrl."

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}
        # inital date for the form
        initial = {}
        # generate the form with the initals
        form = self.form_class(initial=initial)
        # add the form to the context
        context.update({'form': form})
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)
