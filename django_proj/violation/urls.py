from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='violation-home'),
    path('login/', views.login, name='violation-login'),
]
