from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Stock
from app.forms import StockForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_staff) ,login_url="/error/resp")

def index(request):
    assert isinstance(request, HttpRequest)
    Stocks = Stock.objects.all()
    return render(
        request,
        'app/stocks/index.html',
        {
            'Stocks': Stocks
        }
    )

def create(request):
    form = StockForm()
    return render(
        request,
        'app/stocks/create.html',
        {
            'form': form
        }
    )

def store(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," entrees/sorties avec succes ")
        return redirect('/stock')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = StockForm()
        else:
            Stocks = Stock.objects.get(pk=id)
            form = StockForm(instance=Stocks)
        return render(
            request,
            'app/stocks/edit.html',
            {
                'form': form
            }
            )
    else:
        if id == 0:
            form = StockForm(request.POST)
        else:
            Stocks = Stock.objects.get(pk=id)
            form = StockForm(request.POST,instance=Stocks)
        if form.is_valid():
            form.save()
            messages.success(request," Modification du Stock avec succes ")
        return redirect('/stock')
def delete(request, id):
    Stocks = Stock.objects.get(pk=id)
    Stocks.delete()
    messages.success(request," Suppression du stock avec succes ")
    return redirect('/stock')

def getStock_actuel(request):
    id_stock = request.GET.get('id_stock')
    Stocks= Stock.objects.get(pk = id_stock)
    return render(
        request,
        'app/stocks/getStock_actuel.html',
        {
            'Stocks': Stocks
        }
    )