from django.shortcuts import render
from apps.settings.models import Settings,Slide
from apps.tours.models import Tours
from apps.contacts.models import Contacts
from apps.blog.models import Blog

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    tour = Tours.objects.all()
    slide = Slide.objects.latest('id')
    contact = Contacts.objects.latest('id')
    blog = Blog.objects.all()
    
    context = {
        'settings':settings,
        'tour':tour,
        'slide': slide,
        'contact': contact,
        'blog':blog,
        
    }
    return render(request, 'index3.html', context)