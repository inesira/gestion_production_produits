from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Cout_production,Product,Depense
from app.forms import Cout_productionForm,ProductForm
from django.contrib import messages


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