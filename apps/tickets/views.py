from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.tickets.models import Tickets

# Create your views here.
def tickets(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    tickets = Tickets.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'tickets':tickets,
    }
    return render(request, 'destination.html', context)

def tickets_detail(request,id):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    tickets = Tickets.objects.get(id = id)
    
    context = {
        'settings':settings,
        'contact':contact,
        'tickets':tickets,
    }
    return render(request, 'destination-details.html', context)