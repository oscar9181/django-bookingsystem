from django.urls import path
from . import views
urlpatterns = [
    path('base', views.Home, name = 'base'),
    path('', views.Home, name = 'home'),
    
]

