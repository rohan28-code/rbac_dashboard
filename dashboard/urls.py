from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('user/', views.user_dashboard, name='user_dashboard'),

    path('projects/', views.project_list, name='project_list'),

    path('projects/add/', views.project_add, name='project_add'),

    path('projects/edit/<int:id>/', views.project_edit, name='project_edit'),

    path('projects/delete/<int:id>/', views.project_delete, name='project_delete'),
]