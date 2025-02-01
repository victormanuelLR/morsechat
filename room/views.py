from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message, Room
# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room).order_by("-date_added")[:10][::-1]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
