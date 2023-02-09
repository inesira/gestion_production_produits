from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required,user_passes_test
<<<<<<< HEAD
from app.models import Production,Product,Depense,Cout_production
=======
from app.models import Production,Product,Depense,Cout
>>>>>>> feature/data_modeling_update

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")

def index(request):
    assert isinstance(request, HttpRequest)
    count_production = Production.objects.all().count()
    count_product = Product.objects.all().count()
    count_depenses = Depense.objects.all().count()
<<<<<<< HEAD
    Cout_productions = Cout_production.objects.all().order_by()
=======
    Couts = Cout.objects.all().order_by()
>>>>>>> feature/data_modeling_update
  
    
    
    return render(
        request,
        'app/home_resp/index.html',
        {
            'count_production': count_production,
            'count_product': count_product,
            'count_depenses': count_depenses,
<<<<<<< HEAD
            'Cout_productions': Cout_productions,
=======
            'Couts': Couts,
>>>>>>> feature/data_modeling_update
           
            
        }
    ) 
