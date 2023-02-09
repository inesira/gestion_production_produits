from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Production,Product,Depense,Output
from app.forms import ProductionForm,ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")

def index(request):
    assert isinstance(request, HttpRequest)
    Productions = Production.objects.all()
    return render(
        request,
        'app/productions/index.html',
        {
            'Productions': Productions,
        }
    )

def create(request):
    Products = Product.objects.all()
    form = ProductionForm()
    return render(
        request,
        'app/productions/create.html',
        {
            'form': form,
            'Products':Products,
        }
    )

def store(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Entre de la production avec succes ")
        return redirect('/production')
    
# def calcul(request):
#     Outputs = Output.objects.all()
#     Depenses = Depense.objects.all()
#     form = ProductionForm()
#     return render(
#         request,
#         'app/productions/create.html',
#         {
#             'form': form,
#             'Outputs':Outputs,
#             'Depenses':Depenses,
#         }
#     )

# def store_cout(request):
#     if request.method == 'POST':
#         form = ProductionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request," Calcul du cout de production avec succes ")
#         return redirect('/production')    

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Products = Product.objects.all()
    if request.method == "GET":
        if id == 0:
            form = ProductionForm()
        else:
            Productions = Production.objects.get(pk=id)
            form = ProductionForm(instance= Productions)
        return render(
            request,
            'app/productions/edit.html',
            {
                'form': form,
                'Products':Products,
            }
            )

def update(request, id):
    if id == 0:
        form = ProductionForm(request.POST)
    else:
        Productions = Production.objects.get(pk=id)
        form = ProductionForm(request.POST,instance= Productions)
    if form.is_valid():
        form.save()
        messages.success(request," Modification de la production avec succes ")
    return redirect('/production')

def delete(request, id):
    Productions = Production.objects.get(pk=id)
    Productions.delete()
    messages.success(request," Suppression de la production avec succes ")
    return redirect('/production')

def getCout(request):
    id_production = request.GET.get('id_production')
    depenses = Depense.objects.filter(pk = id_production).values('quantite_entree')
    outputs = Output.objects.filter(production_id = id_production).values('quantite_sortie')
    somme =0
    for i in range(0,len(depenses)):
        somme = somme + list(depenses[i].values())[0]
    
    somme_sortie =0  
    for i in range(0,len(outputs)):
        somme_sortie = somme_sortie + list(outputs[i].values())[0]
        
    total = somme + somme_sortie
    return render(
        request,
        'app/outputs/getSorties.html',
        {
            'total': total
        }
    )