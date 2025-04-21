from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='adminLogin'),          
    path('customer/', views.customer, name='customer'),       
    path('admin-login/', views.handleLogin, name='admin-login'), 
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('handleCompanyData/',views.HandleCompanyData,name='handleCompanyData'),
    path('fetchCompanyData/',views.fetchCompanyData,name='fetchCompanyData'),
    path('handleActivate/',views.handleActivity,name="handleActivate"),
    path('details/<int:company_id>/',views.companyHistory,name='companyHistory'),
    path('getCompanies/',views.getCompany,name='getCompany'),
    path('deleteData/',views.deleteData,name='deleteData'),
    path('updatCompanyData/',views.updatCompanyData,name='updatCompanyData'),
    path('update-company/',views.update_company,name='update-company')
]
