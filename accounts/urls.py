from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name="accounts"
urlpatterns = [
    
    path('signup/',views.SignUp.as_view(), name='signup'),
    path('signin/',auth_views.LoginView.as_view(template_name='accounts/signin.html'), name='signin'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    ]