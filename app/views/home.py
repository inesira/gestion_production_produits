from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required,user_passes_test
<<<<<<< HEAD
from app.models import Input,Output,Situation_stock,Stock,Cout_production,Product,Production,Depense
=======
from app.models import Input,Output,MatierePremiere,Cout,Product,Production,Depense
>>>>>>> feature/data_modeling_update

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")
def index(request):
    assert isinstance(request, HttpRequest)
    count_entrees = Input.objects.all().count()
    count_sorties = Output.objects.all().count()
<<<<<<< HEAD
    count_stocks = Stock.objects.all().count()
    count_production = Production.objects.all().count()
    count_product = Product.objects.all().count()
    count_depenses = Depense.objects.all().count()
    Situation_stocks = Situation_stock.objects.all()
    Cout_productions = Cout_production.objects.all()
=======
    count_stocks = MatierePremiere.objects.all().count()
    count_production = Production.objects.all().count()
    count_product = Product.objects.all().count()
    count_depenses = Depense.objects.all().count()
    Outputs = Output.objects.all()
    Couts = Cout.objects.all()
>>>>>>> feature/data_modeling_update
    return render(
        request,
        'app/home/index.html',
        {
            'count_entrees': count_entrees,
            'count_sorties': count_sorties,
            'count_stocks': count_stocks,
            'count_production': count_production,
            'count_product': count_product,
            'count_depenses': count_depenses,
<<<<<<< HEAD
            'Situation_stocks': Situation_stocks,
            'Cout_productions': Cout_productions,
=======
            'Outputs': Outputs,
            'Couts': Couts,
>>>>>>> feature/data_modeling_update
        }
        
    ) 
