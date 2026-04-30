from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    path('logout/',views.logout),

]