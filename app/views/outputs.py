from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Output,Stock
from app.forms import OutputForm,StockForm
from django.contrib import messages

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
    Stocks = Stock.objects.all()
    form = OutputForm()
    return render(
        request,
        'app/outputs/create.html',
        {
            'form': form,
            'Stocks':Stocks,
        }
    )

def store(request):
    if request.method == 'POST':
        form = OutputForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Sortie des Matieres Premieres avec succes ")
        return redirect('/output')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Stocks = Stock.objects.all()
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
                'Stocks':Stocks,
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
    id_stock_id = request.GET.get('id_stock_id')
    stock = Stock.objects.get(pk = id_stock_id)
    return render(
        request,
        'app/outputs/getSorties.html',
        {
            'stock': stock
        }
    )
    
def getPrice(request):
    id_stock_id = request.GET.get('id_stock_id')
    stock = Stock.objects.get(pk = id_stock_id)
    return render(
        request,
        'app/outputs/getPrice.html',
        {
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



    
