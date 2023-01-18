from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Situation_stock,Stock
from app.forms import Situation_stockForm,StockForm
from django.contrib import messages

def index(request):
    assert isinstance(request, HttpRequest)
    Situation_stocks = Situation_stock.objects.all()
    return render(
        request,
        'app/situation_stocks/index.html',
        {
            'Situation_stocks': Situation_stocks,
        }
    )

def create(request):
    Stocks = Stock.objects.all()
    form = Situation_stockForm()
    return render(
        request,
        'app/situation_stocks/create.html',
        {
            'form': form,
            'Stocks':Stocks,
        }
    )

def store(request):
    if request.method == 'POST':
        form = Situation_stockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Situation du Stock actuel avec succes ")
        return redirect('/situation_stock')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Stocks = Stock.objects.all()
    if request.method == "GET":
        if id == 0:
            form = Situation_stockForm()
        else:
            Situation_stocks = Situation_stock.objects.get(pk=id)
            form = Situation_stockForm(instance= Situation_stocks)
        return render(
            request,
            'app/Situation_stocks/edit.html',
            {
                'form': form,
                'Stocks':Stocks,
            }
            )

def update(request, id):
    if id == 0:
        form = Situation_stockForm(request.POST)
    else:
        Situation_stocks = Situation_stock.objects.get(pk=id)
        form = Situation_stockForm(request.POST,instance= Situation_stocks)
    if form.is_valid():
        form.save()
        messages.success(request," Modification du stock actuel avec succes ")
    return redirect('/situation_stock')

def delete(request, id):
    Situation_stocks = Situation_stock.objects.get(pk=id)
    Situation_stocks.delete()
    messages.success(request," annulation de la situation du stock avec succes ")
    return redirect('/situation_stock')

def getStock_actuel(request):
    id_stocks = request.GET.get('id_stocks')
    stock = Stock.objects.get(pk = id_stocks)
    return render(
        request,
        'app/situation_stocks/getStock_actuel.html',
        {
            'stock': stock
        }
    )
    
def getPrix_unitaire(request):
    id_stocks = request.GET.get('id_stocks')
    stock = Stock.objects.get(pk = id_stocks)
    return render(
        request,
        'app/situation_stocks/getPrix_unitaire.html',
        {
            'stock': stock
        }
    )    

def getPrixTotal(request):
    id_stocks = request.GET.get('id_stocks')
    stock = Stock.objects.get(pk = id_stocks)
    
    total = stock.prix_unitaire * stock.stock_actuel
    return render(
        request,
        'app/situation_stocks/getPrixTotal.html',
        {
            'total': total
        }
    )
    
def getDat(request):
    id_stocks = request.GET.get('id_stocks')
    stock = Stock.objects.get(pk = id_stocks)
    return render(
        request,
        'app/situation_stocks/getDat.html',
        {
            'stock': stock
        }
    )     



    
