from django.forms import ModelForm
from app.models import Situation_stock

class Situation_stockForm(ModelForm):
    
    class Meta:
        model = Situation_stock
        fields = '__all__'