from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class UserFormEdit_info(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'