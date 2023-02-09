from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required,user_passes_test
<<<<<<< HEAD
from app.models import Input,Output,Situation_stock,Stock
=======
from app.models import Input,Output,MatierePremiere
>>>>>>> feature/data_modeling_update

# Create your views here.
@login_required( login_url="/")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_staff) ,login_url="/error/resp")
def index(request):
    assert isinstance(request, HttpRequest)
    count_entrees = Input.objects.all().count()
    count_sorties = Output.objects.all().count()
<<<<<<< HEAD
    count_stocks = Stock.objects.all().count()
    Situation_stocks = Situation_stock.objects.all()
=======
    count_stocks = MatierePremiere.objects.all().count()
    Outputs = Output.objects.all()
>>>>>>> feature/data_modeling_update
    return render(
        request,
        'app/home_gest/index.html',
        {
            'count_entrees': count_entrees,
            'count_sorties': count_sorties,
            'count_stocks': count_stocks,
<<<<<<< HEAD
            'Situation_stocks': Situation_stocks,
=======
            'Outputs': Outputs,
>>>>>>> feature/data_modeling_update
        }
    ) 