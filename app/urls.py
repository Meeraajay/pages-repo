from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('login/', views.login_view),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('logout/',views.logout_view),
    path('delete/', views.delete_view),
    path('password/', views.password),
    path('feedback/', views.feedback),
]