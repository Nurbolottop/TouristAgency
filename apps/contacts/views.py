from django.shortcuts import render
from apps.contacts.models import Contacts
from apps.settings.models import Settings

# Create your views here.
def contacts(request):
    contact = Contacts.objects.latest('id')
    settings = Settings.objects.latest('id')
    
    context = {
        'contact': contact,
        'settings':settings,
        
    }
    
    return render(request, 'contact.html', context)