from django.forms import ModelForm
from app.models import Input

class InputForm(ModelForm):
    
    class Meta:
        model = Input
        fields = '__all__'