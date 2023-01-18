from django.shortcuts import render
from apps.settings.models import Settings,Slide
from apps.tours.models import Tours
from apps.contacts.models import Contacts
from apps.blog.models import Blog
from apps.team.models import Team
from apps.tickets.models import Tickets


# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    tour = Tours.objects.all()
    slide = Slide.objects.latest('id')
    contact = Contacts.objects.latest('id')
    blog = Blog.objects.all()
    team = Team.objects.all()
    tickets = Tickets.objects.all()
    
    
    
    context = {
        'settings':settings,
        'tour':tour,
        'slide': slide,
        'contact': contact,
        'blog':blog,
        'team':team,
        'tickets':tickets,
        
        
        
    }
    return render(request, 'index3.html', context)