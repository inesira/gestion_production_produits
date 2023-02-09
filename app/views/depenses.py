from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Depense,Category,Production
from app.forms import DepenseForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")


def index(request):
    assert isinstance(request, HttpRequest)
    Depenses = Depense.objects.all()
    return render(
        request,
        'app/depenses/index.html',
        {
            'Depenses': Depenses,
        }
    )

def create(request):
    Categories = Category.objects.all()
    form = DepenseForm()
    return render(
        request,
        'app/depenses/create.html',
        {
            'form': form,
            'Categories':Categories,
        }
    )

def store(request):
    if request.method == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Insertions des depenses avec succes ")
        return redirect('/depense')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Categories = Category.objects.all()
    if request.method == "GET":
        if id == 0:
            form = DepenseForm()
        else:
            Depenses = Depense.objects.get(pk=id)
            form = DepenseForm(instance= Depenses)
        return render(
            request,
            'app/depenses/edit.html',
            {
                'form': form,
                'Categories':Categories,
            }
            )

def update(request, id):
    if id == 0:
        form = DepenseForm(request.POST)
    else:
        Depenses = Depense.objects.get(pk=id)
        form = DepenseForm(request.POST,instance= Depenses)
    if form.is_valid():
        form.save()
        messages.success(request," Modification des depens avec succes ")
    return redirect('/depense')

def delete(request, id):
    Depenses = Depense.objects.get(pk=id)
    Depenses.delete()
    messages.success(request," Suppression des depenses avec succes ")
    return redirect('/depense')
    
def getDate(request):
    id_production= request.GET.get('id_production')
    production= Production.objects.get(pk = id_production)
    return render(
        request,
        'app/depenses/getDate.html',
        {
            'production': production
        }
    ) 
    
       