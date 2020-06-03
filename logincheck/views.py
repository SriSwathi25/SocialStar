from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
    template_name = 'home.html'

class Welcome(TemplateView):
    template_name = 'welcome.html'

class Thanks(TemplateView):
    template_name = 'thanks.html'