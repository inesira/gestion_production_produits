from django.forms import ModelForm
from app.models import Production

class ProductionForm(ModelForm):
    class Meta:
        model = Production
        fields = '__all__'