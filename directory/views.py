from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Contact

class ContactList(ListView):
    model = Contact
    context_object_name = 'all_contacts'

# def index(request):
#     return render(request, 'index.html')

