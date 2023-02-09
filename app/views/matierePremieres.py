from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import MatierePremiere
from app.forms import MatierePremiereForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/resp")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/gest")

def index(request):
    assert isinstance(request, HttpRequest)
    MatierePremieres = MatierePremiere.objects.all()
    return render(
        request,
        'app/matierePremieres/index.html',
        {
            'MatierePremieres': MatierePremieres
        }
    )

def create(request):
    form = MatierePremiereForm()
    return render(
        request,
        'app/matierePremieres/create.html',
        {
            'form': form
        }
    )

def store(request):
    if request.method == 'POST':
        form = MatierePremiereForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Creation de la Matiere premiere avec succes ")
        return redirect('/matierePremiere')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = MatierePremiereForm()
        else:
            MatierePremieres = MatierePremiere.objects.get(pk=id)
            form = MatierePremiereForm(instance=MatierePremieres)
        return render(
            request,
            'app/matierePremieres/edit.html',
            {
                'form': form
            }
            )
    else:
        if id == 0:
            form = MatierePremiereForm(request.POST)
        else:
            MatierePremieres = MatierePremiere.objects.get(pk=id)
            form = MatierePremiereForm(request.POST,instance=MatierePremieres)
        if form.is_valid():
            form.save()
            messages.success(request," Modification de la Matiere Premiere avec succes ")
        return redirect('/matierePremiere')
def delete(request, id):
    MatierePremieres = MatierePremiere.objects.get(pk=id)
    MatierePremieres.delete()
    messages.success(request," Suppression de la Matiere Premiere avec succes ")
    return redirect('/matierePremiere')
