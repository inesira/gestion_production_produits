from django.shortcuts import redirect,render
from django.http import HttpRequest
<<<<<<< HEAD
from app.models import Output,Stock
from app.forms import OutputForm,StockForm
=======
from app.models import Output,Input
from django.contrib.auth.models import User
from app.forms import OutputForm,InputForm
>>>>>>> feature/data_modeling_update
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
<<<<<<< HEAD
@login_required( login_url="/")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_staff) ,login_url="/error/resp")
=======
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")

>>>>>>> feature/data_modeling_update

def index(request):
    assert isinstance(request, HttpRequest)
    Outputs = Output.objects.all()
    return render(
        request,
        'app/outputs/index.html',
        {
            'Outputs': Outputs,
        }
    )

def create(request):
<<<<<<< HEAD
    Stocks = Stock.objects.all()
=======
    Inputs = Input.objects.all()
>>>>>>> feature/data_modeling_update
    form = OutputForm()
    return render(
        request,
        'app/outputs/create.html',
        {
            'form': form,
<<<<<<< HEAD
            'Stocks':Stocks,
=======
            'Inputs':Inputs,
>>>>>>> feature/data_modeling_update
        }
    )

def store(request):
    if request.method == 'POST':
        form = OutputForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            form.save()
=======
            sortie = int(form['quantite_sortie'].value())
            stocke = float(form['quantite_stock'].value())
            form.save() 
            outputs = Output.objects.all().last()
            sto = stocke - sortie
            outputs.quantite_stock = sto
            outputs.save()
>>>>>>> feature/data_modeling_update
            messages.success(request," Sortie des Matieres Premieres avec succes ")
        return redirect('/output')

def edit(request, id):
    assert isinstance(request, HttpRequest)
<<<<<<< HEAD
    Stocks = Stock.objects.all()
=======
    Inputs = Input.objects.all()
>>>>>>> feature/data_modeling_update
    if request.method == "GET":
        if id == 0:
            form = OutputForm()
        else:
            Outputs = Output.objects.get(pk=id)
            form = OutputForm(instance= Outputs)
        return render(
            request,
            'app/outputs/edit.html',
            {
                'form': form,
<<<<<<< HEAD
                'Stocks':Stocks,
=======
                'Inputs':Inputs,
>>>>>>> feature/data_modeling_update
            }
            )

def update(request, id):
    if id == 0:
        form = OutputForm(request.POST)
    else:
        Outputs = Output.objects.get(pk=id)
        form = OutputForm(request.POST,instance= Outputs)
    if form.is_valid():
        form.save()
        messages.success(request," Modification des Sorties avec succes ")
    return redirect('/output')

def delete(request, id):
    Outputs = Output.objects.get(pk=id)
    Outputs.delete()
    messages.success(request," Suppression des Sorties avec succes ")
    return redirect('/output')

def getSorties(request):
<<<<<<< HEAD
    id_stock_id = request.GET.get('id_stock_id')
    stock = Stock.objects.get(pk = id_stock_id)
=======
    id_matiere_premiere = request.GET.get('id_matiere_premiere')
    inputs = Input.objects.filter(pk = id_matiere_premiere).values('quantite_entree')
    outputs = Output.objects.filter(matiere_premiere_id = id_matiere_premiere).values('quantite_sortie')
    somme =0
    for i in range(0,len(inputs)):
        somme = somme + list(inputs[i].values())[0]
    
    somme_sortie =0  
    for i in range(0,len(outputs)):
        somme_sortie = somme_sortie + list(outputs[i].values())[0]
        
    reste = somme - somme_sortie
>>>>>>> feature/data_modeling_update
    return render(
        request,
        'app/outputs/getSorties.html',
        {
<<<<<<< HEAD
            'stock': stock
=======
            'reste': reste
>>>>>>> feature/data_modeling_update
        }
    )
    
def getPrice(request):
<<<<<<< HEAD
    id_stock_id = request.GET.get('id_stock_id')
    stock = Stock.objects.get(pk = id_stock_id)
=======
    id_matiere_premiere= request.GET.get('id_matiere_premiere')
    input = Input.objects.get(pk = id_matiere_premiere)
>>>>>>> feature/data_modeling_update
    return render(
        request,
        'app/outputs/getPrice.html',
        {
<<<<<<< HEAD
            'stock': stock
        }
    )    

def getPrix_Total(request):
    id_stock_id = request.GET.get('id_stock_id')
    stock = Stock.objects.get(pk = id_stock_id)
    
    total = stock.prix_unitaire * stock.sorties
    return render(
        request,
        'app/outputs/getPrix_Total.html',
        {
            'total': total
        }
    )
    
def getDate(request):
    id_stock_id = request.GET.get('id_stock_id')
    stock = Stock.objects.get(pk = id_stock_id)
    return render(
        request,
        'app/outputs/getDate.html',
        {
            'stock': stock
        }
    )     



    
=======
            'input': input
        }
    ) 
def getDate(request):
    id_matiere_premiere= request.GET.get('id_matiere_premiere')
    input = Input.objects.get(pk = id_matiere_premiere)
    return render(
        request,
        'app/outputs/getDate_entree.html',
        {
            'input': input
        }
    )    
    
def getUnite(request):
    id_matiere_premiere= request.GET.get('id_matiere_premiere')
    input = Input.objects.get(pk = id_matiere_premiere)
    return render(
        request,
        'app/outputs/getUnite.html',
        {
            'input': input
        }
    )       
>>>>>>> feature/data_modeling_update
