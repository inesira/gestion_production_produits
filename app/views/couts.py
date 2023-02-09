from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Cout,Production,Output,Depense
from app.forms import CoutForm,ProductionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")  


def index(request):
    assert isinstance(request, HttpRequest)
    Couts = Cout.objects.all()
    return render(
        request,
        'app/couts/index.html',
        {
            'Couts': Couts,
        }
    )

def create(request):
    Productions = Production.objects.all()
    form = CoutForm()
    return render(
        request,
        'app/couts/create.html',
        {
            'form': form,
            'Productions':Productions,
        }
    )

def store(request):
    if request.method == 'POST':
        form = CoutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," calcule des couts totaux de Production  avec succes ")
        else:
            messages.success(request,form.errors)
        return redirect('/cout')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Productions = Production.objects.all()
    if request.method == "GET":
        if id == 0:
            form = CoutForm()
        else:
            Couts = Cout.objects.get(pk=id)
            form = CoutForm(instance= Couts)
        return render(
            request,
            'app/couts/edit.html',
            {
                'form': form,
                'Productions':Productions,
            }
            )

def update(request, id):
    if id == 0:
        form = CoutForm(request.POST)
    else:
        Couts = Cout.objects.get(pk=id)
        form = CoutForm(request.POST,instance= Couts)
    if form.is_valid():
        form.save()
        messages.success(request," Modification du cout de Productionion avec succes ")
    return redirect('/cout')

def delete(request, id):
    Couts = Cout.objects.get(pk=id)
    Couts.delete()
    messages.success(request," Suppression du cout de Productionion avec succes ")
    return redirect('/cout')

    
    
def getQuantite(request):
    id_production= request.GET.get('id_production')
    production = Production.objects.get(pk = id_production)
    
    return render(
        request,
        'app/couts/getQuantite.html',
        {
            'production': production
        }
    )
    
    
    
def getSortie(request):
    id_production = request.GET.get('id_production')
    output = Output.objects.filter(production_id = id_production).count()
    return render(
        request,
        'app/couts/getSortie.html',
        {
            'output': output
        }
    ) 
    
def getDepense(request):
    id_production = request.GET.get('id_production')
    depense = Depense.objects.filter(production_id = id_production).count()
    return render(
        request,
        'app/couts/getDepense.html',
        {
            'depense': depense
        }
    )
      
def getCoutSortie(request):
    id_production = request.GET.get('id_production')
    outputs = Output.objects.filter(production_id = id_production)
    cout= []
    for output in outputs:
        # cout.append(output.id)
        cout.append(output.prix_total_sortie)
    cout_total_sortie = 0
    for prix_total_sortie in cout:
        cout_total_sortie = cout_total_sortie + prix_total_sortie
    return render(
        request,
        
        'app/couts/getCoutSortie.html',
        {
            'cout_total_sortie': cout_total_sortie
        }
    )          
      
            
def getCoutDepense(request):
    id_production = request.GET.get('id_production')
    depenses = Depense.objects.filter(production_id = id_production)
    cout = []
    for depense in depenses:
        # car_ids.append(mains_d_oeuvres.id)
        cout.append(depense.Prix_total_depense)
    cout_total_depense = 0
    for Prix_total_depense in cout:
        cout_total_depense = cout_total_depense + Prix_total_depense
    return render(
        request,
        
        'app/couts/getCoutDepense.html',
        {
            'cout_total_depense': cout_total_depense
        }
    )    

def getTotal(request):
    id_production= request.GET.get('id_production')
    couts = Cout.objects.filter(production_id = id_production)
    cout_total_production = 0
    for cout in couts:
      cout_total_production= cout.cout_total_sortie + cout.cout_total_depense
    return render(
        request,
        'app/cout_productions/getDepense.html',
        {
            'cout_total_production': cout_total_production
            
        }
    )
    
    
# def getCoutProduction(request):
#     id_production = request.GET.get('id_production')
#     total_production = int(list(Cout.objects.filter(production_id = id_production).values('cout_total_production'))[0]['cout_total_production'])
#     quantite_produite = int(list(Cout.objects.filter(production_id = id_production).values('quantite_produite'))[0]['quantite_produite'])
    
#     quotient = total_production / quantite_produite
    
#     return render(
#         request,
#         'app/couts/getCoutProduction.html',
#         {
#             'quotient': quotient
#         }
#     )
