from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import (
    Create_System_Form,
    Create_Milestone_Form,
    Create_SystemModel_Form,
    Create_MSDBConnention_Form,
)

from django.core.urlresolvers import reverse

from .models import (
    System,
    SystemModel,
    Milestone,
    MSDBConnention,
)

from datetime import datetime




@method_decorator(login_required, name='dispatch')
class Main_View(View):

    template_name = "system/index.html"


    def get(self, request, *args, **kwargs):

        context = {}

        context["system_list"] = System.objects.all()
        context["system_model_list"] = SystemModel.objects.all()
        context["milestone_list"] = Milestone.objects.all()
        context["msdb_connection"] = MSDBConnention.objects.all()


        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class List_All_Systems(View):
    tempalteName = 'system/system_list_view.html'
    panel_titel = 'System List View'

    def get(self, request, *args, **kwargs):
        context = {}

        systemlist = System.objects.all()
        context['system_list'] = systemlist

        context['panel_titel'] = self.panel_titel

        return render(request, self.tempalteName, context)

class Detail_System_View(View):
    templateName = 'system/system_detail_view.html'
    panel_titel = 'System Detail View'

    def get(self, request, *args, **kwargs):
        context = {}

        # system id aus den kwargs holen
        var_system_id = kwargs["pk"]

        var_system_obj_list = System.objects.filter(id=var_system_id)

        if len(var_system_obj_list) != 0:
            context['system'] = var_system_obj_list[0]

        else:
            print("Error: the system is not avalible")

        context['panel_titel'] = self.panel_titel




        return render(request, self.templateName, context)





@method_decorator(login_required, name='dispatch')
class Create_System_View(View):
    form_class = Create_System_Form
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a System'}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            # Hier kann das instance object nochmal geaendert werden
            ## instance.created_user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('system:system_index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)

class Update_System_View(UpdateView):
    form_class = Create_System_Form
    model = System
    template_name = 'system/system_createForm.html'
    success_url = reverse_lazy('system:system_index')

class Delete_System_View(DeleteView):
    model = System
    template_name = "components/component_delete_confirm.html"
    success_url = reverse_lazy('system:system_index')




@method_decorator(login_required, name='dispatch')
class Create_SystemModel_View(View):
    form_class = Create_SystemModel_Form
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a System Model'}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            # Hier kann das instance object nochmal geaendert werden
            ## instance.created_user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('system:system_index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class Create_Milestone_View(View):
    form_class = Create_Milestone_Form
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a Milestone'}

    def get(self, request, *args, **kwargs):

        initial = {
            "creator": request.user,
            "createtion_date": datetime.now(),
        }

        form = self.form_class(initial=initial)
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            # Hier kann das instance object nochmal geaendert werden
            instance.creator = request.user
            instance.createtion_date = datetime.now()

            instance.save()
            return HttpResponseRedirect(reverse('system:system_index'))

        context = {'form': form}
        context.update(self.panel_titel)
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class Create_MSDBConnection_View(View):
    form_class = Create_MSDBConnention_Form
    template_name = 'system/system_createForm.html'
    panel_titel = {'panel_titel' : 'Create a Milestone Time System Connection'}

    def get(self, request, *args, **kwargs):

        initial = {
            "creator": request.user,
            "creation_date": datetime.now(),
        }

        form = self.form_class(initial=initial)
        context = {'form': form}
        context.update(self.panel_titel)
        print(context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        # laden der ausgefuellten form aus dem POST request
        form = self.form_class(request.POST)

        print("---------------------")
        print("-- DEBUG           --")
        print("---------------------")
        print("---------------------")

        # Die System id aus dem POST request laden
        system_id = request.POST["system"]
        # die milestone id aus dem POST request laden
        milestone_id = request.POST["milestone"]

        print(system_id)
        print(milestone_id)
        print("---------------------")


        # Alle Objecte laden die system_id und milestone_id enthalten
        # Denn es darf für jedes system nur ein milesone mit einem type geben
        # nicht das es 2x den MS 10 gibt
        list_msdb_connects = MSDBConnention.objects.filter( system=system_id,
                                                            milestone=milestone_id)
        print("---------------------")
        print(list_msdb_connects)
        print("Anzahl objects vorhanden: {}".format(len(list_msdb_connects)))
        print("---------------------")

        # checken ob die geladene liste objecte enthaelt
        # oder die laenge der liste 0 ist
        if len(list_msdb_connects) != 0:
            error_msg = []
            error_msg.append(str("Es besteht schon ein objekt aus system_id {} und milestone_id {}".format(system_id, milestone_id)))
            print("DEBUG: Error: es ist schon ein Objects dieser Kombination vorhanden")

        else:
            print("DEBUG: OK: Object kann erstellt werden.")

            if form.is_valid():

                instance = form.save(commit=False)

                # Hier kann das instance object nochmal geaendert werden
                ## instance.created_user = request.user

                instance.creator = request.user
                instance.creation_date = datetime.now()

                # hier kann sollte noch ueberprueft werden ob
                #   das datum des Milestone Finish date groeser ist als das datum
                #    der erstellung

                instance.save()
                return HttpResponseRedirect(reverse('system:system_index'))


        context = {'form': form}
        context.update(self.panel_titel)
        context.update({"error_msg_avalible": True})
        context.update({"error_msg_list": error_msg})
        return render(request, self.template_name, context)
