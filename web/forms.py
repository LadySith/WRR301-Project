from django import forms
from django.contrib.auth.forms import UserCreationForm
from web.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, required=False)
    last_name = forms.CharField(max_length=32, required=False)
    email = forms.EmailField(max_length=254, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
