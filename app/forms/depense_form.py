from django.forms import ModelForm
from app.models import Depense

class DepenseForm(ModelForm):
    
    class Meta:
        model = Depense
        fields = '__all__'