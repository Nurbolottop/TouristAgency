from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.team.models import Team
# Create your views here.
def teams(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    team = Team.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'team':team,
    }
    return render(request, 'guide.html', context)