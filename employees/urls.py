from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('employees/<int:pk>/restore/', views.employee_restore, name='employee_restore'),
    path('employees/<int:pk>/permanent-delete/', views.employee_permanent_delete, name='employee_permanent_delete'),
]