from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Depense,Production,Output
from app.forms import DepenseForm,ProductionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")


def index(request):
    assert isinstance(request, HttpRequest)
    Depenses = Depense.objects.all()
    return render(
        request,
        'app/depense_admin/index.html',
        {
            'Depenses': Depenses,
        }
    )