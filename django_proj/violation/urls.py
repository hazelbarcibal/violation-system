from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='violation-home'),
    path('login/', views.login, name='violation-login'),
    path('innerpage/', views.innerpage, name='violation-innerpage'),
    path('scan/', views.scan, name='violation-scan')
]
