from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Input,MatierePremiere
from app.forms import InputForm,MatierePremiereForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")

def index(request):
    assert isinstance(request, HttpRequest)
    Inputs = Input.objects.all()
    return render(
        request,
        'app/inputs/index.html',
        {
            'Inputs': Inputs,
        }
    )

def create(request):
    MatierePremieres = MatierePremiere.objects.all()
    form = InputForm()
    return render(
        request,
        'app/inputs/create.html',
        {
            'form': form,
            'MatierePremieres':MatierePremieres,
        }
    )

def store(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Entre des matieres premieres avec succes ")
        return redirect('/input')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    MatierePremieres = MatierePremiere.objects.all()
    if request.method == "GET":
        if id == 0:
            form = InputForm()
        else:
            Inputs = Input.objects.get(pk=id)
            form = InputForm(instance= Inputs)
        return render(
            request,
            'app/inputs/edit.html',
            {
                'form': form,
                'MatierePremieres':MatierePremieres,
            }
            )

def update(request, id):
    if id == 0:
        form = InputForm(request.POST)
    else:
        Inputs = Input.objects.get(pk=id)
        form = InputForm(request.POST,instance= Inputs)
    if form.is_valid():
        form.save()
        messages.success(request," Modification des Entrees avec succes ")
    return redirect('/input')

def delete(request, id):
    Inputs = Input.objects.get(pk=id)
    Inputs.delete()
    messages.success(request," Suppression des Entrees avec succes ")
    return redirect('/input')



    
