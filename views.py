#-*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView

'''def home(request):
    return render(request, 'investivgroup/accueil.html', {})'''

class home(TemplateView):
   template_name = "investivgroup/accueil.html"  # chemin vers le template à afficher

#def qui_sommes_nous(request):
    #return render(request, 'investivgroup/apropos.html',{})

def services(request):
    return render(request, 'investivgroup/services.html',{})

def projet_agricole(request):
    return render(request, 'investivgroup/pj_agricole.html',{})

class contact(TemplateView):
    template_name = "investivgroup/contact.html"

