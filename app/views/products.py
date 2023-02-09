from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Product
from app.forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
<<<<<<< HEAD
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
=======
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")
>>>>>>> feature/data_modeling_update

def index(request):
    assert isinstance(request, HttpRequest)
    Products = Product.objects.all()
    return render(
        request,
        'app/products/index.html',
        {
            'Products': Products
        }
    )
<<<<<<< HEAD
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")    
=======
>>>>>>> feature/data_modeling_update

def create(request):
    form = ProductForm()
    return render(
        request,
        'app/products/create.html',
        {
            'form': form
        }
    )
<<<<<<< HEAD
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")    
=======
>>>>>>> feature/data_modeling_update

def store(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Insertion d'un produit fini avec succes ")
        return redirect('/product')
<<<<<<< HEAD
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")    
=======
    
>>>>>>> feature/data_modeling_update

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            Products = Product.objects.get(pk=id)
            form = ProductForm(instance=Products)
        return render(
            request,
            'app/products/edit.html',
            {
                'form': form
            }
            )
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            Products = Product.objects.get(pk=id)
            form = ProductForm(request.POST,instance=Products)
        if form.is_valid():
            form.save()
            messages.success(request," Modification du Produit fini avec succes ")
        return redirect('/product')
<<<<<<< HEAD
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")    
=======
    
>>>>>>> feature/data_modeling_update
def delete(request, id):
    Products = Product.objects.get(pk=id)
    Products.delete()
    messages.success(request," Suppression d'un Produit fini avec succes ")
    return redirect('/product')
