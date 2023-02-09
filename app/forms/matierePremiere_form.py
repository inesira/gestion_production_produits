from django.forms import ModelForm
from app.models import MatierePremiere

class MatierePremiereForm(ModelForm):
    
    class Meta:
        model = MatierePremiere
        fields = '__all__'