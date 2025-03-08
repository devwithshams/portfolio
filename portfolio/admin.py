from django.contrib import admin
from .models import Project, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    readonly_fields = ('created',)

admin.site.register(Project)
admin.site.register(Contact, ContactAdmin)  # Use ContactAdmin here
