from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Production
from app.forms import ProductionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")

def index(request):
    assert isinstance(request, HttpRequest)
    Productions = Production.objects.all()
    return render(
        request,
        'app/productions/index.html',
        {
            'Productions': Productions
        }
    )

def create(request):
    form = ProductionForm()
    return render(
        request,
        'app/productions/create.html',
        {
            'form': form
        }
    )

def store(request):
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," creation d'une production avec succes ")
        return redirect('/production')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProductionForm()
        else:
            Productions = Production.objects.get(pk=id)
            form = ProductionForm(instance=Productions)
        return render(
            request,
            'app/productions/edit.html',
            {
                'form': form
            }
            )
    else:
        if id == 0:
            form = ProductionForm(request.POST)
        else:
            Productions = Production.objects.get(pk=id)
            form = ProductionForm(request.POST,instance=Productions)
        if form.is_valid():
            form.save()
            messages.success(request," Modification de la Production avec succes ")
        return redirect('/production')
def delete(request, id):
    Productions = Production.objects.get(pk=id)
    Productions.delete()
    messages.success(request," Suppression de la production avec succes ")
    return redirect('/production')

