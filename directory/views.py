from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import timedelta, date
from django.db.models import Q

from .models import Contact
from .forms import ContactForm

class ContactList(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        today = date.today()
        one_month = today + timedelta(days=30)

        birthdays = Contact.objects.filter(username=self.request.user).filter(Q(birthday__month=today.month, birthday__day__gte=today.day) | Q(birthday__month=today.month+1)).filter(self_contact=False).order_by('-birthday__month').order_by('-birthday__day')[:5]
        all_contacts = Contact.objects.filter(username=self.request.user).order_by('last_name')
        return render(request, 'directory/contact_list.html', {'all_contacts':all_contacts, 'birthdays':birthdays})

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
    # context_object_name = 'contact'

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_info'] = Contact.objects.filter(username=self.request.user).filter(self_contact=True).values()[0]
        return context

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