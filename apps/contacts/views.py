from django.shortcuts import render
from apps.contacts.models import Contacts
from apps.settings.models import Settings
from apps.gallery.models import Gallery

# Create your views here.
def contacts(request):
    contact = Contacts.objects.latest('id')
    settings = Settings.objects.latest('id')
    gallery = Gallery.objects.all()
    
    context = {
        'contact': contact,
        'settings':settings,
        'gallery':gallery,
        
    }
    
    return render(request, 'contact.html', context)