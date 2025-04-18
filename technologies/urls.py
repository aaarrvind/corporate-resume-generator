from django.urls import path
from . import views

urlpatterns = [
    path('coding-languages/', views.coding_language_list, name='coding_language_list'),
    path('coding-languages/create/', views.coding_language_create, name='coding_language_create'),
    path('coding-languages/<int:pk>/update/', views.coding_language_update, name='coding_language_update'),
    path('coding-languages/<int:pk>/delete/', views.coding_language_delete, name='coding_language_delete'),
    path('coding-languages/<int:pk>/restore/', views.coding_language_restore, name='coding_language_restore'),
    path('coding-languages/<int:pk>/permanent-delete/', views.coding_language_permanent_delete, name='coding_language_permanent_delete'),
    path('tools/', views.tool_list, name='tool_list'),
    path('tools/create/', views.tool_create, name='tool_create'),
    path('tools/<int:pk>/update/', views.tool_update, name='tool_update'),
    path('tools/<int:pk>/delete/', views.tool_delete, name='tool_delete'),
    path('tools/<int:pk>/restore/', views.tool_restore, name='tool_restore'),
    path('tools/<int:pk>/permanent-delete/', views.tool_permanent_delete, name='tool_permanent_delete'),
]