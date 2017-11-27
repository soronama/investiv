from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView

class home(TemplateView):
   template_name = "investivgroup/accueil.html"

#def qui_sommes_nous(request):
    #return render(request, 'investivgroup/apropos.html',{})

def services(request):
    return render(request, 'investivgroup/services.html',{})

def projet_agricole(request):
    return render(request, 'investivgroup/pj_agricole.html',{})

class contact(TemplateView):
    template_name = "investivgroup/contact.html"

