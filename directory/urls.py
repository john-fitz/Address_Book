from django.urls import include, path
from . import views
from .views import ContactList, ContactView

urlpatterns = [
    path('', ContactList.as_view(), name='show-contacts'),
    path('add-contact/', views.contact_req, name='add-contact'),
    path('contacts/<int:pk>', ContactView.as_view(), name='contact-detail'),
]