from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name',)
        # 'date_joined','last_joined','is_superuser','is_staff','is_active')