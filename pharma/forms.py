from django import forms
from .models import Ville, Periode

class FilterForm(forms.Form):
    ville = forms.ModelChoiceField(
        queryset=Ville.objects.all(),
        label="Ville",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Sélecionné la ville'})
    )
    
    periode = forms.ModelChoiceField(
        queryset=Periode.objects.all(),
        label="Période",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Sélecionné la période'})
    )
