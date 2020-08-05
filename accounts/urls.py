from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

app_name="accounts"
urlpatterns = [
    path('index/',views.index, name='index'),
    path('signup/',views.SignUp.as_view(), name='signup'),
    path('signin/',auth_views.LoginView.as_view(template_name='accounts/signin.html'), name='signin'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    ]