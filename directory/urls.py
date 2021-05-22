from django.urls import path
from . import views
from .views import ContactList

urlpatterns = [
    path('', ContactList.as_view(), name='show-contacts'),
]