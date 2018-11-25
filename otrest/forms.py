from django import forms
from .models import OtRequest, OtRecord

class OtRequestForm(forms.ModelForm):
    class Meta:
        model = OtRequest
        fields = ("ottime","reason",)

class OtRecordForm(forms.ModelForm):
    class Meta:
        model = OtRecord
        fields = ("startTime","endTime",)
