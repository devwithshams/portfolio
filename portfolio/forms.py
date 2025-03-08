from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):  # Change TodoForm to ContactForm
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
