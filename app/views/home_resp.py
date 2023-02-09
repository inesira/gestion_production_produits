from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required,user_passes_test
from app.models import Production,Product,Depense,Cout

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")

def index(request):
    assert isinstance(request, HttpRequest)
    count_production = Production.objects.all().count()
    count_product = Product.objects.all().count()
    count_depenses = Depense.objects.all().count()
    Couts = Cout.objects.all().order_by()
  
    
    
    return render(
        request,
        'app/home_resp/index.html',
        {
            'count_production': count_production,
            'count_product': count_product,
            'count_depenses': count_depenses,
            'Couts': Couts,
           
            
        }
    ) 
