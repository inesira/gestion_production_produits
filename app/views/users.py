from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from app.forms import UserForm

# Display users
def index(request,id):
    users = User.objects.filter(pk = id).order_by('username')
    return render(
        request,
        'app/users/index.html',
        {
            'users': users
        }
    )
    
# Show register form
def register(request):
    form = UserForm()
    return render(
        request, 
        'app/users/register.html',
        {
            'form': form
        }
    )
    
def update(request,id):
    if id == 0:
        form = UserForm(request.POST)
    else:
        users = User.objects.get(pk=id)
        form = UserForm(request.POST,instance= users)
    if form.is_valid():
        form.save()
        messages.success(request," Modification du profil avec succes ")
        return redirect('/')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            users = User.objects.get(pk=id)
            form = UserForm(instance= users)
        return render(
            request,
            'app/users/edit.html',
            {
                'form': form
            }
            )

# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password incorrect')
            
    return render(
        request,
        'app/users/login.html'
    )

# Register a new user    
def store(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Insertion avec succes')
        return redirect('/')
  
# Logout a user authenticated  
def user_logout(request):
    logout(request)
    return redirect('/')