from django import forms
from .models import BusinessDetails, Client, State, County
from django.core.exceptions import ValidationError
from .models import Employee
from .models import Project
# Custom widget for currency input
class CurrencyInput(forms.NumberInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'form-control currency-input', 'placeholder': '$0.00', 'step': '0.01'}
        super().__init__(*args, **kwargs)

# Form for BusinessDetails model
class BusinessDetailsForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.filter(is_deleted=False), label="Select Client")
    # Add empty labels for better UX
    state = forms.ModelChoiceField(
        queryset=State.objects.all(), 
        widget=forms.Select(attrs={'id': 'state-dropdown', 'class': 'form-control'}),
        empty_label="Select a State"
    )
    county = forms.ModelChoiceField(
        queryset=County.objects.none(),
        widget=forms.Select(attrs={'id': 'county-dropdown', 'class': 'form-control'}),
        empty_label="Select a County"
    )

    class Meta:
        model = BusinessDetails
        fields = [
            'received_on', 'assigned_on', 
            'batch_type', 'order_no', 'borrower_name_1', 'borrower_name_2',
            'address', 'state', 'county', 'Origination_date', 'loan_amount', 'product', 'status','completed_on',
            'processor_name', 'typing', 'completed_on',  'Qcer'
        ]
        widgets = {
            'received_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'assigned_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'completed_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'Origination_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'loan_amount': CurrencyInput(),
            'batch_type': forms.TextInput(attrs={'class': 'form-control'}),
            'order_no': forms.TextInput(attrs={'class': 'form-control'}),
            'borrower_name_1': forms.TextInput(attrs={'class': 'form-control'}),
            'borrower_name_2': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'processor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'typing': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.TextInput(attrs={'class': 'form-control'}),
            'Qcer': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['county'].queryset = County.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['county'].queryset = County.objects.none()
        elif self.instance.pk:
            self.fields['county'].queryset = self.instance.state.county_set.order_by('name')
        else:
            # Initially disable the county field
            self.fields['county'].widget.attrs.update({'disabled': 'disabled'})

    def clean(self):
        cleaned_data = super().clean()
        assigned_on = cleaned_data.get("assigned_on")
        completed_on = cleaned_data.get("completed_on")

        if completed_on and assigned_on and completed_on <= assigned_on:
            raise ValidationError("Completed On Date must be after Assigned On Date.")
        
        return cleaned_data


# Form for Client model
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name', 'last_name','company_name', 'email', 'phone', 'address'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'role', 'email', 'phone']



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'status', 'start_date', 'end_date']  # Add any other project fields you have