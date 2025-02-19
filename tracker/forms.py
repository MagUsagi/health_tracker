from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import HealthRecord

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['date', 'weight', 'temperature', 'menstruation']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "mx-auto w-100 w-md-50 p-4 shadow rounded bg-light"
        self.helper.layout = Layout(
            HTML('<h2 class="text-center mb-4">Enter Health Data</h2>'),
            Div(FloatingField('date'), css_class="form-floating mb-3"),
            Div(FloatingField('weight'), css_class="form-floating mb-3"),
            Div(FloatingField('temperature'), css_class="form-floating mb-3"),
            Div(
                'menstruation',
                css_class="form-check form-switch align-items-center mt-3"
            ),
            Div(
                Submit('submit', 'Save', css_class='btn btn-primary w-50'),
                css_class="text-center mt-3"
            )
        )

        # 最新の menstruation 値を取得
        latest_record = HealthRecord.objects.order_by('-date').first()
        if latest_record:
            self.fields['menstruation'].initial = latest_record.menstruation