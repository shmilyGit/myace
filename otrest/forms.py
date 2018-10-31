from django import forms
from .models import OtRest

class OtRestForm(forms.ModelForm):
    class Meta:
        model = OtRest 
        fields = ("ottime","reason",)
