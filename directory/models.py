from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    # phone_number = models.DateTimeField('Last Updated') 
    #can use a new field called phone-number-field that you need to install
    email = models.EmailField(blank=True, null=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    notes = models.TextField('Notes', max_length=500, blank=True) 

    def __str__(self):
        return (self.first_name + " " + self.last_name)