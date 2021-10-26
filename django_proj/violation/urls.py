from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='violation-home'),
    path('login/', views.login, name='violation-login'),
    path('innerpage/', views.innerpage, name='violation-innerpage'),
    path('scan/', views.scan, name='violation-scan'),
<<<<<<< HEAD
    path('v_table/', views.v_table, name='violation-v_table')
=======
    path('create/', views.create, name='violation-create')
>>>>>>> 21a99974e26b021aba6ce6adf7a901ea15d58675
]
