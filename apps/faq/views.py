from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.faq.models import Faq

# Create your views here.
def faq(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    faq = Faq.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'faq':faq,
    }
    return render(request, 'faq.html', context)
