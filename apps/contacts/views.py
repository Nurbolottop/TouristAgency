from django.shortcuts import render
from apps.contacts.models import Contacts

# Create your views here.
def contacts(request):
    contact = Contacts.objects.latest('id')
    
    context = {
        'contact': contact,
        
    }
    
    return render(request, 'contact.html', context)