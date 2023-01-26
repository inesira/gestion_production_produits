from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Mains_d_oeuvres,Category
from app.forms import Main_d_oeuvreForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")

def index(request):
    assert isinstance(request, HttpRequest)
    Main_d_oeuvres = Mains_d_oeuvres.objects.all()
    return render(
        request,
        'app/main_d_oeuvres/index.html',
        {
            'Main_d_oeuvres': Main_d_oeuvres,
        }
    )

def create(request):
    Categories = Category.objects.all()
    form = Main_d_oeuvreForm()
    return render(
        request,
        'app/main_d_oeuvres/create.html',
        {
            'form': form,
            'Categories':Categories,
        }
    )

def store(request):
    if request.method == 'POST':
        form = Main_d_oeuvreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Insertion de la main d'oeuvre avec succes ")
        return redirect('/mains_d_oeuvres')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Categories = Category.objects.all()
    if request.method == "GET":
        if id == 0:
            form = Main_d_oeuvreForm()
        else:
            Main_d_oeuvres = Mains_d_oeuvres.objects.get(pk=id)
            form = Main_d_oeuvreForm(instance= Main_d_oeuvres)
        return render(
            request,
            'app/main_d_oeuvres/edit.html',
            {
                'form': form,
                'Categories':Categories,
            }
            )

def update(request, id):
    if id == 0:
        form = Main_d_oeuvreForm(request.POST)
    else:
        Main_d_oeuvres = Mains_d_oeuvres.objects.get(pk=id)
        form = Main_d_oeuvreForm(request.POST,instance= Main_d_oeuvres)
    if form.is_valid():
        form.save()
        messages.success(request," Modification de  la main d'oeuvre avec succes ")
    return redirect('/mains_d_oeuvres')

def delete(request, id):
    Main_d_oeuvres = Mains_d_oeuvres.objects.get(pk=id)
    Main_d_oeuvres.delete()
    messages.success(request," Suppression de la main d'oeuvre avec succes ")
    return redirect('/mains_d_oeuvres')

def getRevenu(request):
    id_category = request.GET.get('id_category')
    category = Category.objects.get(pk = id_category)
    return render(
        request,
        'app/main_d_oeuvres/getRevenu.html',
        {
            'category': category
        }
    )





    
