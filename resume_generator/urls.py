from django.urls import path
from company import views

  # replace 'core' with your app name


urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.company_profile, name='company_profile'),
]
