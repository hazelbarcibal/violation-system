from django.urls import path
from . import views

#app_name = 'violation'
urlpatterns = [
    path('', views.home, name='violation-home'),
    path('signin/', views.signin, name='violation-signin'),
    path('sign-up/', views.signup, name='violation-signup'),
    path('logout/', views.logoutUser, name='violation-logout'),
    path('home/', views.innerpage, name='violation-innerpage'),
    path('scanQR/', views.scanQR, name='violation-scanQR'),
    path('createQR/', views.createQR, name='violation-createQR'),
    path('student/about/', views.studentAbout, name='violation-studentAbout'),
    path('student/home/', views.studentHome, name='violation-studentHome'),
    path('student/view-violation-list/', views.studentViolation, name='violation-studentViolation'),
    path('add-violation/', views.add, name='violation-addViolation'),
    path('violation-list/', views.table, name='violation-list'),
    path('update-record/<int:pk>/', views.edit, name='violation-edit'),

]
