from django.shortcuts import render
from apps.settings.models import Settings,Slide
from apps.tours.models import Tours
from apps.contacts.models import Contacts
from apps.blog.models import Blog
from apps.team.models import Team
from apps.tickets.models import Tickets
from apps.review.models import Review
from apps.gallery.models import Gallery

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    tour = Tours.objects.all()
    slide = Slide.objects.latest('id')
    contact = Contacts.objects.latest('id')
    blog = Blog.objects.all()
    team = Team.objects.all()
    tickets = Tickets.objects.all()
    review = Review.objects.all()
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'tour':tour,
        'slide': slide,
        'contact': contact,
        'blog':blog,
        'team':team,
        'tickets':tickets,
        'review':review,
        'gallery':gallery,
        
    }
    return render(request, 'index3.html', context)