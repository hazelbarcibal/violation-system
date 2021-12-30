from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Records
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class addViolation(ModelForm):
    class Meta:
        model = Records
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'required': True, 'placeholder': 'Email'}),
        }
        