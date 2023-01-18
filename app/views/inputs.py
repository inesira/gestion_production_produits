from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Input,Stock
from app.forms import InputForm,StockForm
from django.contrib import messages

def index(request):
    assert isinstance(request, HttpRequest)
    Inputs = Input.objects.all()
    return render(
        request,
        'app/inputs/index.html',
        {
            'Inputs': Inputs,
        }
    )

def create(request):
    Stocks = Stock.objects.all()
    form = InputForm()
    return render(
        request,
        'app/inputs/create.html',
        {
            'form': form,
            'Stocks':Stocks,
        }
    )

def store(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Entre des matieres premieres avec succes ")
        return redirect('/input')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Stocks = Stock.objects.all()
    if request.method == "GET":
        if id == 0:
            form = InputForm()
        else:
            Inputs = Input.objects.get(pk=id)
            form = InputForm(instance= Inputs)
        return render(
            request,
            'app/inputs/edit.html',
            {
                'form': form,
                'Stocks':Stocks,
            }
            )

def update(request, id):
    if id == 0:
        form = InputForm(request.POST)
    else:
        Inputs = Input.objects.get(pk=id)
        form = InputForm(request.POST,instance= Inputs)
    if form.is_valid():
        form.save()
        messages.success(request," Modification des Entrees avec succes ")
    return redirect('/input')

def delete(request, id):
    Inputs = Input.objects.get(pk=id)
    Inputs.delete()
    messages.success(request," Suppression des Entrees avec succes ")
    return redirect('/input')

def getEntrees(request):
    id_stock = request.GET.get('id_stock')
    stock = Stock.objects.get(pk = id_stock)
    return render(
        request,
        'app/inputs/getEntrees.html',
        {
            'stock': stock
        }
    )
    
def getTotal(request):
    id_stock = request.GET.get('id_stock')
    stock = Stock.objects.get(pk = id_stock)
    return render(
        request,
        'app/inputs/getTotal.html',
        {
            'stock': stock
        }
    )    
def getTotale(request):
    id_stock = request.GET.get('id_stock')
    stock = Stock.objects.get(pk = id_stock)
    
    total = stock.prix_unitaire * stock.entrees
    return render(
        request,
        'app/inputs/getTotale.html',
        {
            'total': total
        }
    ) 
    
def getDate(request):
    id_stock = request.GET.get('id_stock')
    stock = Stock.objects.get(pk = id_stock)
    return render(
        request,
        'app/inputs/getDate.html',
        {
            'stock': stock
        }
    )         
   
    





    
