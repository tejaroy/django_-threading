# forms.py
from django import forms
from Apps.App.models import *


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = "__all__"
