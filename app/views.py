from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserForm
from .models import Room, Message


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist!!")
            return redirect("login")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Password !!")
    return render(request, 'app/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')    
    

def registerPage(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, "Passwords are not the same!!")
        elif len(password1) < 8:
            messages.error(request, "Password must have minimum 8 length!!")
        elif form.is_valid() == False:
            messages.error(request, "Username is already exist!!")
        else:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'app/register.html', context)

def home(request):
    if request.method == 'POST':
        roomName = request.POST['roomName']
        roomName = roomName.lower()
        if roomName.strip() != "":
            return redirect('room', roomName=roomName)
    return render(request, "app/index.html", {})

@login_required(login_url='login')
def room(request, roomName):
    room, created = Room.objects.get_or_create(name=roomName)
    room_messages = [] if created else room.message_set.all()
    context = {'roomName':roomName, 'room_messages':room_messages}     
    return render(request, 'app/room.html', context)
