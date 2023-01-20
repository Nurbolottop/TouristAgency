from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.team.models import Team
from apps.gallery.models import Gallery

# Create your views here.
def teams(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    team = Team.objects.all()
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'team':team,
        'gallery':gallery,
        
    }
    return render(request, 'guide.html', context)