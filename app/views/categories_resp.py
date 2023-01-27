from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Category
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")

def index(request):
    assert isinstance(request, HttpRequest)
    Categories = Category.objects.all()
    return render(
        request,
        'app/categories_resp/index.html',
        {
            'Categories': Categories
        }
    )