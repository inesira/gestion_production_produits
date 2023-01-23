from django.forms import ModelForm
from app.models import Cout_production

class Cout_productionForm(ModelForm):
    
    class Meta:
        model = Cout_production
        fields = '__all__'