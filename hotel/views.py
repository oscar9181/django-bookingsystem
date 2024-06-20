from django.shortcuts import render
from .models import Room

# Create your views here.
def Home(request):
    
    return render(request, 'Home/home.html',{})


def room_view(request):
    available = Room.objects.all()
    return render(request, 'Home/room.html',{'all': available}) 

  