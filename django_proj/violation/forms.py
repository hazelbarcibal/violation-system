from django.forms import ModelForm
from .models import Records


class Violation(ModelForm):
    class Meta:
        model = Records
        fields = '__all__'