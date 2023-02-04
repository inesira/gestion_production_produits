from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Cout_production,Product,Depense
from app.forms import Cout_productionForm,ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")

def index(request):
    assert isinstance(request, HttpRequest)
    Cout_productions = Cout_production.objects.all()
    return render(
        request,
        'app/cout_production_admin/index.html',
        {
            'Cout_productions': Cout_productions,
        }
    )    