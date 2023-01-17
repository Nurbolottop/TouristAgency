from django.shortcuts import render
from apps.settings.models import Settings,Slide
from apps.tours.models import Tours
from apps.contacts.models import Contacts

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    tour = Tours.objects.all()
    slide = Slide.objects.latest('id')
    contact = Contacts.objects.latest('id')
    context = {
        'settings':settings,
        'tour':tour,
        'slide': slide,
        'contact': contact,
        
    }
    return render(request, 'index3.html', context)