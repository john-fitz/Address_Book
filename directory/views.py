from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import redirect

from .models import Contact
from .forms import ContactForm

class ContactList(ListView):
    model = Contact
    context_object_name = 'all_contacts'
    ordering = ['-last_name']

class UpdateContactView(UpdateView):
    model = Contact
    context_object_name = 'contact'
    form_class = ContactForm
    template_name = 'directory/add_contact.html'

    def form_valid(self, form):
        contact = form.save()  
        return redirect('contact-detail', pk=contact.pk)

class ContactView(DetailView):
    model = Contact
    context_object_name = 'contact'

class AddContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'directory/add_contact.html'

    def form_valid(self, form):
        contact = form.save()  
        return redirect('contact-detail', pk=contact.pk)
