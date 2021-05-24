from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404


from .models import Contact
from .forms import ContactForm

class ContactList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    context_object_name = 'all_contacts'
    # ordering = ['-last_name']
    
    def get_queryset(self):
        return Contact.objects.filter(username=self.request.user)

class UpdateContactView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    context_object_name = 'contact'
    form_class = ContactForm
    template_name = 'directory/add_contact.html'

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user

    def form_valid(self, form):
        contact = form.save()  
        return redirect('contact-detail', pk=contact.pk)

class ContactView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Contact
    context_object_name = 'contact'

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user

class AddContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'directory/add_contact.html'

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.username = self.request.user
        contact.save()  
        return redirect('contact-detail', pk=contact.pk)

class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    template_name = 'directory/delete_contact.html'
    context_object_name = 'contact'
    success_url = reverse_lazy('show-contacts')
    
    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)