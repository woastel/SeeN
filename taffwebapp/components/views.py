from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from datetime import datetime
from .models import (
                Component)


@method_decorator(login_required, name='dispatch')
class MainView(View):
    templateName = 'components/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        usernameRequest = self.request.user.username




        return render(request, self.templateName, context)


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
