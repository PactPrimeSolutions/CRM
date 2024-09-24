# myapp/widgets.py
from django import forms

class CurrencyInput(forms.NumberInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'form-control currency-input', 'placeholder': '$0.00'}
        super().__init__(*args, **kwargs)
