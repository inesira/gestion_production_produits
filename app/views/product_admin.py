from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Product
from app.forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")

def index(request):
    assert isinstance(request, HttpRequest)
    Products = Product.objects.all()
    return render(
        request,
        'app/product_admin/index.html',
        {
            'Products': Products
        }
    )