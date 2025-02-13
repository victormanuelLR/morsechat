from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .forms import SignUpForm, CreateRoom
from room.models import Room
# Create your views here.

def principalpage(request):
    if request.method == "POST":
        form = CreateRoom(request.POST)
        if form.is_valid():
            roomname = form.cleaned_data["roomname"]
            slugname= slugify(roomname.lower().replace(" ", "-"), allow_unicode=True)

            Room.objects.get_or_create(name=roomname, slug=slugname)

            return redirect("room")

    else:
        return render(request, 'core/principalpage.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('principalpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})