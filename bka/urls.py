from django.urls import path
from bka import views
 
urlpatterns = [

    path('', views.login_page, name="login_page"),
    
    path('logout_page/', views.logout_page, name="logout_page"),

    path('change_password/', views.change_password, name="change_password"),

    path('add_installation_informations/', views.add_installation_informations, name='add_installation_informations'),

    path('add_validation/', views.add_validation, name='add_validation'),

    path('update_validation/<int:pk>/', views.update_validation, name='update_validation'),

    path('ajax/load-services/', views.load_services, name='ajax_load_services'),

    path('cancel_validation/<int:pk>/', views.cancel_validation, name='cancel_validation'),

    path('edit_coordinates/<int:pk>/', views.edit_coordinates, name='edit_coordinates'),

    path('list_coordinates/', views.list_coordinates, name='list_coordinates'),

    path('delete_coordinates/<int:pk>/', views.delete_coordinates, name='delete_coordinates'),

    path('list_coordinates_pmo/', views.list_coordinates_pmo, name='list_coordinates_pmo'),

    path('list_validations/', views.list_validations, name='list_validations'),

    path('list_valid_informations/', views.list_valid_informations, name='list_valid_informations'),

    path('list_valid_informations_pmo/', views.list_valid_informations_pmo, name='list_valid_informations_pmo'),
]
