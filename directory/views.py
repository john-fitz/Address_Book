from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


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

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'directory/delete_contact.html'
    context_object_name = 'contact'
    success_url = reverse_lazy('show-contacts')

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)