from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Cout_production,Product,Depense
from app.forms import Cout_productionForm,ProductForm
from django.contrib import messages

def index(request):
    assert isinstance(request, HttpRequest)
    Cout_productions = Cout_production.objects.all()
    return render(
        request,
        'app/cout_productions/index.html',
        {
            'Cout_productions': Cout_productions,
        }
    )

def create(request):
    Products = Product.objects.all()
    form = Cout_productionForm()
    return render(
        request,
        'app/cout_productions/create.html',
        {
            'form': form,
            'Products':Products,
        }
    )

def store(request):
    if request.method == 'POST':
        form = Cout_productionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," calcule du cout de production  avec succes ")
        return redirect('/cout_production')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Products = Product.objects.all()
    if request.method == "GET":
        if id == 0:
            form = Cout_productionForm()
        else:
            Cout_productions = Cout_production.objects.get(pk=id)
            form = Cout_productionForm(instance= Cout_productions)
        return render(
            request,
            'app/cout_productions/edit.html',
            {
                'form': form,
                'Products':Products,
            }
            )

def update(request, id):
    if id == 0:
        form = Cout_productionForm(request.POST)
    else:
        Cout_productions = Cout_production.objects.get(pk=id)
        form = Cout_productionForm(request.POST,instance= Cout_productions)
    if form.is_valid():
        form.save()
        messages.success(request," Modification du cout de production avec succes ")
    return redirect('/cout_production')

def delete(request, id):
    Cout_productions = Cout_production.objects.get(pk=id)
    Cout_productions.delete()
    messages.success(request," Suppression du cout de production avec succes ")
    return redirect('/cout_production')

def getProduct(request):
    id_Product = request.GET.get('id_Product')
    product = Product.objects.get(pk = id_Product)
    return render(
        request,
        'app/cout_productions/getProduct.html',
        {
            'product': product
        }
    )
    
    
def getDepense(request):
    id_depense= request.GET.get('id_depense')
    depense = Depense.objects.get(pk = id_depense)
    
    cout_total_pro= depense.cout_total_sorties + depense.cout_total_m
    return render(
        request,
        'app/cout_productions/getDepense.html',
        {
            'cout_total_pro': cout_total_pro
        }
    )
    
    
    
def getDate(request):
    id_depense = request.GET.get('id_depense')
    depense = Depense.objects.get(pk = id_depense)
    return render(
        request,
        'app/cout_productions/getDate.html',
        {
            'depense': depense
        }
    ) 
    
def getUnite(request):
    id_Product = request.GET.get('id_Product')
    product = Product.objects.get(pk = id_Product)
    return render(
        request,
        'app/cout_productions/getUnite.html',
        {
            'product': product
        }
    )
            


