from django.shortcuts import redirect,render
from django.http import HttpRequest
<<<<<<< HEAD
from app.models import Production
from app.forms import ProductionForm
=======
from app.models import Production,Product,Depense,Output
from app.forms import ProductionForm,ProductForm
>>>>>>> feature/data_modeling_update
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
    Productions = Production.objects.all()
    return render(
        request,
        'app/productions/index.html',
        {
<<<<<<< HEAD
            'Productions': Productions
=======
            'Productions': Productions,
>>>>>>> feature/data_modeling_update
        }
    )

def create(request):
<<<<<<< HEAD
=======
    Products = Product.objects.all()
>>>>>>> feature/data_modeling_update
    form = ProductionForm()
    return render(
        request,
        'app/productions/create.html',
        {
<<<<<<< HEAD
            'form': form
=======
            'form': form,
            'Products':Products,
>>>>>>> feature/data_modeling_update
        }
    )

def store(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            form.save()
<<<<<<< HEAD
            messages.success(request," creation d'une production avec succes ")
        return redirect('/production')

def edit(request, id):
    assert isinstance(request, HttpRequest)
=======
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
>>>>>>> feature/data_modeling_update
    if request.method == "GET":
        if id == 0:
            form = ProductionForm()
        else:
            Productions = Production.objects.get(pk=id)
<<<<<<< HEAD
            form = ProductionForm(instance=Productions)
=======
            form = ProductionForm(instance= Productions)
>>>>>>> feature/data_modeling_update
        return render(
            request,
            'app/productions/edit.html',
            {
<<<<<<< HEAD
                'form': form
            }
            )
    else:
        if id == 0:
            form = ProductionForm(request.POST)
        else:
            Productions = Production.objects.get(pk=id)
            form = ProductionForm(request.POST,instance=Productions)
        if form.is_valid():
            form.save()
            messages.success(request," Modification de la Production avec succes ")
        return redirect('/production')
=======
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

>>>>>>> feature/data_modeling_update
def delete(request, id):
    Productions = Production.objects.get(pk=id)
    Productions.delete()
    messages.success(request," Suppression de la production avec succes ")
    return redirect('/production')

<<<<<<< HEAD
=======
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
>>>>>>> feature/data_modeling_update
