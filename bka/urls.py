from django.urls import path
from bka import views
 
urlpatterns = [

    path('login/', views.login, name="login"),
    
    path('logout/', views.logout, name="logout"),

    path('add_installation_informations/', views.add_installation_informations, name='add_installation_informations'),

    path('edit_installation_informations/<int:pk>/', views.edit_installation_informations, name='edit_installation_informations'),

    path('edit_coordinates/<int:pk>/', views.edit_coordinates, name='edit_coordinates'),

    path('list_coordinates/', views.list_coordinates, name='list_coordinates'),

    path('list_all_informations/', views.list_all_informations, name='list_all_informations'),
]
