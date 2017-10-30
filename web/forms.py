from django import forms
from django.contrib.auth.forms import UserCreationForm
from web.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, required=True)
    last_name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField(max_length=254, required=True)

    def clean_email(self):
        submitted_data = self.cleaned_data['email']
        if ('@nmmu.ac.za' or '@mandela.ac.za') not in submitted_data:
            raise forms.ValidationError('You must register using a valid university email address')
        return submitted_data

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
