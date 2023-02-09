from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required,user_passes_test
from app.models import Input,Output,MatierePremiere,Cout,Product,Production,Depense

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")
def index(request):
    assert isinstance(request, HttpRequest)
    count_entrees = Input.objects.all().count()
    count_sorties = Output.objects.all().count()
    count_stocks = MatierePremiere.objects.all().count()
    count_production = Production.objects.all().count()
    count_product = Product.objects.all().count()
    count_depenses = Depense.objects.all().count()
    Outputs = Output.objects.all()
    Couts = Cout.objects.all().order_by()
    
    cou_ords =[]
    cou_dates =[]
    cou_prices = []
    l_dates = Cout.objects.values('quantite_produite')
    liste_dates = []
    liste_services = []
    l_prices = Cout.objects.values('cout_production')
    # li_services = Car_service.objects.values('service_id')
    
    for i in range(0, len(l_prices)):
        cou_prices.append(list(l_prices[i].values())[0])
        
    for i in range(0, len(l_dates)):
        liste_dates.append(list(l_dates[i].values())[0])
    # l_date=Order.objects.values(id)
    
    # for li_service in li_services:
    #     liste_services.append(Order.objects.filter(car_service_id = li_service).count())
        
    for cou_or in Couts :
        dates = []
        if cou_or.quantite_produite is not dates:
            dates.append(cou_or.quantite_produite)
            n = 0
            cou_ords.append(Cout.objects.filter(quantite_produite = cou_or.quantite_produite).count())
            cous = Cout.objects.filter(quantite_produite = cou_or.quantite_produite).values('cout_production')
            cou_dates.append(cou_or.quantite_produite)
            cou_dates.append(cou_or.production)
            for i in range(0, len(cous)):
                n = n + list(cous[i].values())[0]
            cou_prices.append(n)
        
    lis_serv=Production.objects.values('pk')
    lis_serves = []
    na_services = Production.objects.values('produit_fini')
    name_services = []
    
    for i in range(0, len(na_services)):
        name_services.append(list(na_services[i].values())[0])
        
    for i in range(0, len(lis_serv)):
        lis_serves.append(list(lis_serv[i].values())[0])
        
    # lis_serv_eng = Service_engineer.objects.filter(service_id = lis_serve).values('pk')
    # lis_serv_engs = []
    
    # for i in range(0, len(lis_serv_eng)):
    #     lis_serv_engs.append(list(lis_serv_eng[i].values())[0])
        
    for lis_serve in lis_serves:
        liste_services.append(Production.objects.filter(produit_fini = lis_serve).values('pk'))
    
    
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
            'Outputs': Outputs,
            'Couts': Couts,
            'cou_ords': cou_ords,
            'cou_dates': cou_dates,
            'cou_prices': cou_prices,
            'liste_dates': liste_dates,
            'liste_services': liste_services, 
            'name_services': name_services,
        }
        
    ) 
