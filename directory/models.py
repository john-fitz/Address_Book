from django.db import models
from django.contrib.auth.models import User
# from address.models import AddressField


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    notes = models.TextField('Notes', max_length=500, blank=True) 
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length = 50, null=True, blank=True)
    address_line2 = models.CharField(max_length = 50, null=True, blank=True)
    address_ZIP = models.CharField(max_length = 5, null=True, blank=True)
    address_state = models.CharField(max_length = 50, null=True, blank=True)
    self_contact = models.BooleanField(default=False)
    

    def __str__(self):
        return (self.first_name + " " + self.last_name)