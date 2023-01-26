from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserFormEdit(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'is_superuser',
            'is_staff',
        ]