from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from accounts import forms
from django.urls import reverse, reverse_lazy
# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:signin')
    template_name='accounts/signup.html'






