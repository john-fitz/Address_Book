from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper

class DateInput(forms.DateInput):
    input_type = 'date'


class ContactForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Contact

        fields = (
            'first_name', 'last_name', 'email', 'birthday', 'notes', 'address_line1', 'address_line2', 'address_ZIP',
            'address_state',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Main St'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment or Suite #'}),
            'address_ZIP': forms.NumberInput(attrs={'class': 'form-control'}),
            'address_state': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'address_line1': 'Address 1',
            'address_line2': 'Address 2 (optional)',
            'address_ZIP': 'Zip code',
            'address_state': 'State',
        }