from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.tickets.models import Tickets
from apps.gallery.models import Gallery

# Create your views here.
def tickets(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    tickets = Tickets.objects.all()
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'tickets':tickets,
        'gallery':gallery,
        
    }
    return render(request, 'destination.html', context)

def tickets_detail(request,id):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    tickets = Tickets.objects.get(id = id)
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'tickets':tickets,
        'gallery':gallery,
        
    }
    return render(request, 'destination-details.html', context)