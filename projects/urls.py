from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('projects/<int:pk>/restore/', views.project_restore, name='project_restore'),
    path('projects/<int:pk>/permanent-delete/', views.project_permanent_delete, name='project_permanent_delete'),
]