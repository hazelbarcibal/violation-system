from django import forms
from django.forms import ModelForm
from .models import Records
#from django.urls import reverse

class addViolation(ModelForm):
    class Meta:
        model = Records
        fields = '__all__'