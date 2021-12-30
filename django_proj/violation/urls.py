from django.urls import path
from . import views

#app_name = 'violation'
urlpatterns = [
    path('', views.home, name='violation-home'),
    path('signin/', views.signin, name='violation-signin'),
    path('register/', views.register, name='violation-register'),
    path('logout/', views.logoutUser, name='violation-logout'),
    path('innerpage/', views.innerpage, name='violation-innerpage'),
    path('scan/', views.scan, name='violation-scan'),
    path('create/', views.create, name='violation-create'),
    #path('v_table/', views.v_table, name='violation-v_table'),
    path('add/', views.add, name='violation-add'),
    path('table/', views.table, name='violation-table'),
    path('edit/<int:pk>/', views.edit, name='violation-edit'),
]
