from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.gallery.models import Gallery

# Create your views here.
def gallery(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'gallery':gallery,
        
    }
    return render(request, 'gallary.html', context)