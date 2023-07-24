from django.urls import path
from bka import views
 
urlpatterns = [

    path('login/', views.login, name="login"),
    
    path('logout/', views.logout, name="logout"),

    path('add_installation_information/', views.add_installation_information, name='add_installation_information'),

    path('edit_installation_information/<int:pk>/', views.edit_installation_information, name='edit_installation_information'),

    path('list_coordinates/', views.list_coordinates, name='list_coordinates'),

    path('list_all_informations/', views.list_all_informations, name='list_all_informations'),
]
