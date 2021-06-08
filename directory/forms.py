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
            'first_name', 'last_name', 'email', 'birthday', 'notes', 
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }