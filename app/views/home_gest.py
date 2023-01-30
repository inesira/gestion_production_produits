from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required,user_passes_test
from app.models import Input,Output,Situation_stock,Stock

# Create your views here.
@login_required( login_url="/")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_staff) ,login_url="/error/resp")
def index(request):
    assert isinstance(request, HttpRequest)
    count_entrees = Input.objects.all().count()
    count_sorties = Output.objects.all().count()
    count_stocks = Stock.objects.all().count()
    Situation_stocks = Situation_stock.objects.all()
    return render(
        request,
        'app/home_gest/index.html',
        {
            'count_entrees': count_entrees,
            'count_sorties': count_sorties,
            'count_stocks': count_stocks,
            'Situation_stocks': Situation_stocks,
        }
    ) 