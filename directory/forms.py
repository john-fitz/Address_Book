from django import forms
from django.forms import ModelForm
from .models import Contact

class DateInput(forms.DateInput):
    input_type = 'date'


class ContactForm(ModelForm):
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
            'birthday': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }