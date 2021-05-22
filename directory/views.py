from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect

from .models import Contact
from .forms import ContactForm

class ContactList(ListView):
    model = Contact
    context_object_name = 'all_contacts'

class ContactView(DetailView):
    model = Contact
    context_object_name = 'contact'


def contact_req(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/?submitted=True')
        
        else:
            form = ContactForm()
            if 'submitted' in request.GET:
                submitted = True
    
    # really not sure about this part - should redirect to detailed view of contact
    return render(request, 'directory/contact.html', {'form': form, 'contact_info': Contact.objects.all(), 'submitted': submitted})


