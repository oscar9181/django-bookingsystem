from django.shortcuts import render,redirect,get_object_or_404
from .models import Room

# Create your views here.
def Home(request):
    
    return render(request, 'Home/home.html',{})


def room_view(request):
    available = Room.objects.all()
    return render(request, 'Home/room.html',{'all': available}) 

def room_detail(request, room_id):
    room =get_object_or_404(Room, id=room_id)

    print('logged ins',request.user)
    return render(request, 'Home/room-detail.html',{'Room': room}) 