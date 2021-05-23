from django.urls import include, path
from . import views
from .views import ContactList, ContactView, AddContactView

urlpatterns = [
    path('', ContactList.as_view(), name='show-contacts'),
    path('add-contact/', AddContactView.as_view(), name='add-contact'),
    path('contacts/<int:pk>', ContactView.as_view(), name='contact-detail'),
]