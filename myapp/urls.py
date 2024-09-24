from django.urls import path
from .views import (
    base_view, download_excel, generate_report, 
    delete_business_detail, restore_business_detail, retrieve_deleted
)
from django.conf import settings
from django.conf.urls.static import static
from .views import calendar_view
from .views import events_view
from .views import event_list
from . import views
from .views import  add_client_view, delete_client_view, deleted_clients_view, restore_client_view
from .views import client_list, add_client, edit_client, delete_client, restore_client,client_detail

from .views import download_excel

urlpatterns = [
    path('', base_view, name='base'),
    path('download-excel/', download_excel, name='download_excel'),
    path('generate-report/', generate_report, name='generate_report'),
    path('delete-business-detail/<int:pk>/', delete_business_detail, name='delete_business_detail'),
    path('restore-business-detail/<int:pk>/', restore_business_detail, name='restore_business_detail'),
    path('retrieve-deleted/', retrieve_deleted, name='retrieve_deleted_business'),
    path('calendar/', calendar_view, name='calendar'),
    path('events/', event_list, name='event_list'),  # Add this line
    path('calendar/add/', views.add_event, name='add_event'),
    path('calendar/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('calendar/restore/<int:event_id>/', views.restore_event, name='restore_event'),

    
    
     path('load-counties/', views.load_counties, name='load_counties'),


  path('clients/', client_list, name='client_list'),
    path('clients/add/', add_client, name='add_client'),  # Make sure this points to add_client
    path('clients/edit/<int:client_id>/', edit_client, name='edit_client'),
    path('clients/delete/<int:client_id>/', delete_client, name='delete_client'),
    path('clients/restore/<int:client_id>/', restore_client, name='restore_client'),
    path('clients/<int:client_id>/', client_detail, name='client_detail'),
    path('download-excel/', download_excel, name='download_excel'),
     path('clients/<int:client_id>/add-employee/', views.add_employee, name='add_employee'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
     path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('employee/<int:employee_id>/edit/', views.edit_employee, name='edit_employee'),
    path('employee/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),


    path('projects/add/<int:client_id>/', views.add_project, name='add_project'),
    path('projects/edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('events/', events_view, name='events'),
]