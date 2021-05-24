from django.urls import include, path
from . import views
from .views import ContactList, ContactView, AddContactView, UpdateContactView, ContactDeleteView

urlpatterns = [
    path('', ContactList.as_view(), name='show-contacts'),
    path('add-contact/', AddContactView.as_view(), name='add-contact'),
    path('update_contact/<int:pk>', UpdateContactView.as_view(), name='update-contact'),
    path('delete_contact/<int:pk>', ContactDeleteView.as_view(), name='delete-contact'),
    path('contacts/<int:pk>', ContactView.as_view(), name='contact-detail'),
]