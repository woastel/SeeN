from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from datetime import datetime
from .models import (
                Component,
                Component_Type,
                Component_cable_charackter,
                Component_thermal_charackter,
                Component_mechanik_charackter,
                Component_electronik_charackter)


@method_decorator(login_required, name='dispatch')
class MainView(View):
    templateName = 'components/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        usernameRequest = self.request.user.username


        context["componentTypeList"] = Component_Type.objects.all()

        # init a component type dictonary
        componentTypeCountDict = []
        # loop throug the component type list
        # to add items into the component type dictionary
        for item in context["componentTypeList"]:
            count1 = Component.objects.filter(component_type=item).count()
            var_dict ={"name":item.name, "count":count1}
            componentTypeCountDict.append(var_dict)
            print(var_dict)

        context["componentTypeCountDict"] = componentTypeCountDict
        print(context["componentTypeCountDict"])






        ## DEBUG
        #component_list_dict = {}
        #for comp in context["componentTypeList"]:
        #    liste = Component.objects.filter(component_type__name=comp.name)
        #    temp_dict = {comp.name:liste}
        #    component_list_dict.update(temp_dict)


        #for comptype in component_list_dict:
        #    print("Component Type: " + str(comptype))
        #    for comp in component_list_dict[comptype]:
        #        print("\t - " + str(comp.name))


        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Component_List_View(View):
    template_name = 'components/component_list_view.html'

    def get(self, request, *args, **kwargs):
        username_request = self.request.user.username
        context = {}

        context["component_list"] = Component.objects.all()
        print(context["component_list"])

        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Component_Create_View(View):
    form_class_component = forms.Form_Component
    form_class_thermal_charackter = forms.Form_Component_thermal_charackter
    form_class_electronik_charackter = forms.Form_Component_electronik_charackter
    form_class_mechanik_charackter = forms.Form_Component_mechanik_charackter
    form_class_cable_charackter = forms.Form_Component_cable_charackter

    template_name = 'components/component_create.html'

    def get(self, request, *args, **kwargs):

        context = {}

        initial = {
            "user_creator" : request.user,
            "user_updater" : request.user,
            "date_creation" : datetime.now(),
            "date_update" : datetime.now(),}


        form_component = self.form_class_component(initial=initial)
        context.update({'form_component': form_component})

        form_thermal_charackter = self.form_class_thermal_charackter()
        context.update({'form_thermal_charackter': form_thermal_charackter})

        form_electronik_charackter = self.form_class_electronik_charackter()
        context.update({'form_electronik_charackter': form_electronik_charackter})

        form_mechanik_charackter = self.form_class_mechanik_charackter()
        context.update({'form_mechanik_charackter': form_mechanik_charackter})

        form_cable_charackter = self.form_class_cable_charackter()
        context.update({'form_cable_charackter': form_cable_charackter})

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form_component = self.form_class_component(request.POST)
        form_thermal_charackter = self.form_class_thermal_charackter(request.POST)
        form_electronik_charackter = self.form_class_electronik_charackter(request.POST)
        form_mechanik_charackter = self.form_class_mechanik_charackter(request.POST)
        form_cable_charackter = self.form_class_cable_charackter(request.POST)

        if form_component.is_valid():
            instance_component = form_component.save(commit=False)
            instance_component.created_user = request.user

            # if instance_component.thermal_charakter_avalible is True:
            if form_thermal_charackter.is_valid():
                instance_thermal_charackter = form_thermal_charackter.save(commit=False)
                instance_thermal_charackter.save()
                instance_component.thermal_charakter = instance_thermal_charackter

            # if instance_component.electronic_charakter_avalible == True:
            if form_electronik_charackter.is_valid():
                instance_electronik_charackter = form_electronik_charackter.save(commit=False)
                instance_electronik_charackter.save()
                instance_component.electronic_charakter = instance_electronik_charackter

            # if instance_component.mechanic_charakter_avalible == True:
            if form_mechanik_charackter.is_valid():
                instance_mechanic_charackter = form_mechanik_charackter.save(commit=False)
                instance_mechanic_charackter.save()
                instance_component.mechanic_charakter = instance_mechanic_charackter

            # if instance_component.cable_charakter_avalible == True:
            if form_cable_charackter.is_valid():
                instance_cable_charackter = form_cable_charackter.save(commit=False)
                instance_cable_charackter.save()
                print(type(instance_cable_charackter))
                instance_component.cable_charakter = instance_cable_charackter

            instance_component.save()

            return HttpResponseRedirect(reverse('components:index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class Component_Detail_View(View):
    template_name = 'components/component_detail_view.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context["alert_danger_avalible"] = False

        # get the component id from the kwargs -- key = "pk"
        component_id = kwargs["pk"]

        component = Component.objects.filter(id=component_id)
        try:
            component = component[0]
            context["component"] = component
        except:
            context["alert_danger_avalible"] = True
            context["alert_danger"] = "Error: Component List is empty"

        username_request = self.request.user.username

        return render(request, self.template_name, context)
