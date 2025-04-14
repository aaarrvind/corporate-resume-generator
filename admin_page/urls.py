from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='adminLogin'),          
    path('home/', views.home, name='home'),       
    path('admin-login/', views.handleLogin, name='admin-login'), 
]
