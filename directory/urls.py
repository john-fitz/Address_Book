from django.urls import path
from . import views
from .views import ContactList, ContactView

urlpatterns = [
    path('', ContactList.as_view(), name='show-contacts'),
    path('contacts/<int:pk>', ContactView.as_view(), name='contact-detail')
]