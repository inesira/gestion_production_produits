from django.forms import ModelForm
from app.models import Cout

class CoutForm(ModelForm):
    
    class Meta:
        model = Cout
        fields = '__all__'