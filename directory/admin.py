from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name')


admin.site.register(Contact, ContactAdmin)