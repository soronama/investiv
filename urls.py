from django.conf.urls import url, patterns, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^accueil$', views.home.as_view()),
    url(r'^apropos', TemplateView.as_view(template_name='investivgroup/apropos.html')),
    url(r'^services$', views.services),
    url(r'^projet$', views.projet_agricole),
    url(r'^contact$', views.contact.as_view()),
]
