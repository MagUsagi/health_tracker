from django import forms
from .models import HealthRecord
from datetime import date

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['date', 'weight', 'temperature', 'menstruation']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': date.today().strftime('%Y-%m-%d')}),
            'weight': forms.NumberInput(attrs={'step': '0.1'}),
            'temperature': forms.NumberInput(attrs={'step': '0.01'}),
        }