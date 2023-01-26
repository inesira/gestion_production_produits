from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Mains_d_oeuvres,Category
from app.forms import Main_d_oeuvreForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required( login_url="/login")
@user_passes_test(lambda user: user.is_staff ,login_url="/error/gest")
@user_passes_test(lambda user: user.is_superuser ,login_url="/error/resp")

def index(request):
    assert isinstance(request, HttpRequest)
    Main_d_oeuvres = Mains_d_oeuvres.objects.all()
    return render(
        request,
        'app/main_d_oeuvres_admin/index.html',
        {
            'Main_d_oeuvres': Main_d_oeuvres,
        }
    )
