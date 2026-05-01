from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('logout/',views.logout),
    path('delete/', views.delete),
    path('password/', views.password),
]