from django.urls import path
from . import views
urlpatterns = [
    # path('base', views.base, name = 'base'),
    path('', views.Home, name = 'home'),
    path('rooms',views.room_view, name='room'),
    
]

