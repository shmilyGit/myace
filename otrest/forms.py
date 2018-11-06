from django import forms
from .models import OtRequest

class OtRequestForm(forms.ModelForm):
    class Meta:
        model = OtRequest
        fields = ("ottime","reason",)
