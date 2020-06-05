from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from accounts import forms
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
import misaka


from django.contrib.auth import views as auth_views
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:signin')
    template_name='accounts/signup.html'
    def form_valid(self,form):
        subject = "Welcome to Social Star Family"
        #message = misaka.html("<h1>Welcome dear" +form.cleaned_data["username"]+" !!</h1><br/><p><strong>You can write blogs, create groups, add posts, join and leave groups.</strong></p><br/><h2>Happy Blogging :)</h2>")
        message_html = render_to_string("email.html",{'name':form.cleaned_data["username"]})
        message = strip_tags(message_html)
        from_email = '25nsriswathi@gmail.com'
        to_email = form.cleaned_data['email']
        fail_silently = False
        #send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[to_email,], fail_silently=fail_silently)
        mail = EmailMultiAlternatives(subject, message, from_email, [to_email,])
        mail.attach_alternative(message_html,"text/html")
        mail.send()

        return super(SignUp,self).form_valid(form)

class LoginView(auth_views.LoginView):
    def __init__(self,*args,**kwargs):
        self.request.session.set_expire_at_browser_close = True
        






