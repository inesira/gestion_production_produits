from django.forms import ModelForm
from app.models import Output

class OutputForm(ModelForm):
    class Meta:
        model = Output
        fields = '__all__'