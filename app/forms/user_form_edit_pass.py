from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class UserFormEditPass(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'