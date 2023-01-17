from django.shortcuts import render
from apps.tours.models import Tours
from apps.settings.models import Settings
from apps.contacts.models import Contacts

# Create your views here.

def tour(request):
    tour = Tours.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    
    context = {
        'settings':settings,
        'tour':tour,
        'contact': contact,
    }
    return render(request,'package.html',context)

def tour_detail(request,id):
    tour = Tours.objects.get(id = id)   
    contact = Contacts.objects.latest('id')
    
    settings = Settings.objects.latest('id')
    context = {
        'settings':settings,
        'tour':tour,
        'contact': contact,

    }
    return render(request,'package-details.html',context)