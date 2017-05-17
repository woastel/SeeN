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
        Pcie_Ctrl)


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

@method_decorator(login_required, name='dispatch')
class List_Component_View(View):
    templateName = 'components/component_list_view.html'
    panel_titel = "Component List View"

    def get(self, request, *args, **kwargs):
        # context that schould be render
        context = {}

        context["component_list"] = Component.objects.all()
        nearby_places = Component.objects.filter(character_thermal_avalible=True).select_subclasses()

        print("\n\n----------------------")

        for i in nearby_places:
            print(str(i) + " Temp: " + str(i.temperature_max))

        print("----------------------\n\n")

        print(context["component_list"])
        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
        return render(request, self.templateName, context)

@method_decorator(login_required, name='dispatch')
class Detail_Component_View(View):
    templateName = 'components/component_detail_view.html'
    panel_titel = "Component Detail View"

    def get(self, request, *args, **kwargs):
        # context dictonary - render context
        context = {}
        context['alert_success_avalible'] = False
        context['alert_danger_avalible'] = False
        # component id
        var_component_id = kwargs["pk"]
        # get the component - but select the subclasses
        var_component = Component.objects.filter(component_id=var_component_id).select_subclasses()

        # put the component into the dictonary
        # check if the querysert has a object
        if len(var_component) != 0:
            context['component'] = var_component[0]
            context['alert_success_avalible'] = True
            context['alert_success'] = str(
                'Pass - Component with id({}) is avalible.'.format(var_component_id))
        else:
            context['alert_danger_avalible'] = True
            context['alert_danger'] = str(
                'Error - Component with id({}) isnt avalible.'.format(var_component_id))


        # add the panel titel to the context
        context.update({'panel_titel': self.panel_titel})
        # now return the render object with template name and context
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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            ## -- this instance have no creator instance.created_user = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            ## -- this instance have no creator instance.created_user = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)


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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)


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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

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

    def post(self, request, *args, **kwargs):
        # first save the form with the request Post arguments
        form = self.form_class(request.POST)
        print(request.POST)

        # check if form is valid
        if form.is_valid():
            # then get the instance from the form without commit
            instance = form.save(commit=False)
            # change some attributes from the instance
            instance.date_creation = datetime.now()
            instance.date_update = datetime.now()
            instance.user_creator = request.user
            instance.user_updater = request.user
            # save the instance
            instance.save()
            # return a http redirect
            return HttpResponseRedirect(reverse('components:index'))

        # if form is not valid - return the form object like the
        #  get method
        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)
