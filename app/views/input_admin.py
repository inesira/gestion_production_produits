from django.shortcuts import redirect,render
from django.http import HttpRequest
<<<<<<< HEAD
from app.models import Input,Stock
from app.forms import InputForm,StockForm
=======
from app.models import Input
from app.forms import InputForm
>>>>>>> feature/data_modeling_update
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
        'app/input_admin/index.html',
        {
            'Inputs': Inputs,
        }
    )
