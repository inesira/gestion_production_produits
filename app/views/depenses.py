from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Depense,Production,Output,Mains_d_oeuvres
from app.forms import DepenseForm,ProductionForm
from django.contrib import messages

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
    Productions = Production.objects.all()
    form = DepenseForm()
    return render(
        request,
        'app/depenses/create.html',
        {
            'form': form,
            'Productions':Productions,
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
    Productions = Production.objects.all()
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
                'Productions':Productions,
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
    
def getCategories(request):
    id_production = request.GET.get('id_production')
    mains_d_oeuvres = Mains_d_oeuvres.objects.filter(production_id = id_production).count()
    return render(
        request,
        'app/depenses/getCategories.html',
        {
            'mains_d_oeuvres': mains_d_oeuvres
        }
    ) 
    
    
def getTotal_m(request):
    id_production = request.GET.get('id_production')
    main_d_oeuvres = Mains_d_oeuvres.objects.filter(production_id = id_production)
    cout = []
    for mains_d_oeuvres in main_d_oeuvres:
        # car_ids.append(mains_d_oeuvres.id)
        cout.append(mains_d_oeuvres.total)
    cout_total_m = 0
    for total in cout:
        cout_total_m = cout_total_m + total
    return render(
        request,
        
        'app/depenses/getTotal_m.html',
        {
            'cout_total_m': cout_total_m
        }
    )    
       
def getStocks(request):
    id_production = request.GET.get('id_production')
    output = Output.objects.filter(production_id = id_production).count()
    return render(
        request,
        'app/depenses/getStocks.html',
        {
            'output': output
        }
    )

    
def getDate(request):
    id_production = request.GET.get('id_production')
    production = Production.objects.get(pk = id_production)
    return render(
        request,
        'app/depenses/getDate.html',
        {
            'production': production
        }
    )         
   
def getTotal_sorties(request):
    id_production = request.GET.get('id_production')
    outputs = Output.objects.filter(production_id = id_production)
    cout= []
    for output in outputs:
        # cout.append(output.id)
        cout.append(output.total)
    cout_total_sorties = 0
    for total in cout:
        cout_total_sorties = cout_total_sorties + total
    return render(
        request,
        
        'app/depenses/getTotal_sorties.html',
        {
            'cout_total_sorties': cout_total_sorties
        }
    )    
      





    
