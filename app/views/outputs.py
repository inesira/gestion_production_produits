from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Output,Input
from django.contrib.auth.models import User
from app.forms import OutputForm,InputForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/")
@user_passes_test(lambda user: not(user.is_superuser) ,login_url="/error/admin")
@user_passes_test(lambda user: not(user.is_staff) ,login_url="/error/resp")

def index(request):
    assert isinstance(request, HttpRequest)
    Outputs = Output.objects.all()
    return render(
        request,
        'app/outputs/index.html',
        {
            'Outputs': Outputs,
        }
    )

def create(request):
    Inputs = Input.objects.all()
    form = OutputForm()
    return render(
        request,
        'app/outputs/create.html',
        {
            'form': form,
            'Inputs':Inputs,
        }
    )

def store(request):
    if request.method == 'POST':
        form = OutputForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Sortie des Matieres Premieres avec succes ")
        return redirect('/output')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    Inputs = Input.objects.all()
    if request.method == "GET":
        if id == 0:
            form = OutputForm()
        else:
            Outputs = Output.objects.get(pk=id)
            form = OutputForm(instance= Outputs)
        return render(
            request,
            'app/outputs/edit.html',
            {
                'form': form,
                'Inputs':Inputs,
            }
            )

def update(request, id):
    if id == 0:
        form = OutputForm(request.POST)
    else:
        Outputs = Output.objects.get(pk=id)
        form = OutputForm(request.POST,instance= Outputs)
    if form.is_valid():
        form.save()
        messages.success(request," Modification des Sorties avec succes ")
    return redirect('/output')

def delete(request, id):
    Outputs = Output.objects.get(pk=id)
    Outputs.delete()
    messages.success(request," Suppression des Sorties avec succes ")
    return redirect('/output')

def getSorties(request):
    id_matiere_premiere = request.GET.get('id_matiere_premiere')
    input = Input.objects.get(pk = id_matiere_premiere)
    return render(
        request,
        'app/outputs/getSorties.html',
        {
            'input': input
        }
    )
    
def getPrice(request):
    id_matiere_premiere= request.GET.get('id_matiere_premiere')
    input = Input.objects.get(pk = id_matiere_premiere)
    return render(
        request,
        'app/outputs/getPrice.html',
        {
            'input': input
        }
    ) 
    
def getUser(request):
    
    user = User.objects.get(pk = id)
    return render(
        request,
        'app/outputs/getUser.html',
        {
            'user': user
        }
    )       