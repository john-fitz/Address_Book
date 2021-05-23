from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import Contact
from .forms import ContactForm

class ContactList(ListView):
    model = Contact
    context_object_name = 'all_contacts'

class ContactView(DetailView):
    model = Contact
    context_object_name = 'contact'


# def contact_req(request):
#     submitted = False
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/?submitted=True')
        
#     else:
#         form = ContactForm()
#         if 'submitted' in request.GET:
#             submitted = True
    
#     # really not sure about this part - should redirect to detailed view of contact
#     return render(request, 'directory/contact.html', {'form': form})

class AddContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'directory/add_contact.html'

    def form_valid(self, form):
        employee = form.save()  
        return redirect('show-contacts')
