from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")

def index(request):
    return render(
        request,
        'app/home_resp/index.html'
    ) 
