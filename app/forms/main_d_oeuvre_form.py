from django.forms import ModelForm
from app.models import Mains_d_oeuvres

class Main_d_oeuvreForm(ModelForm):
    class Meta:
        model = Mains_d_oeuvres
        fields = '__all__'