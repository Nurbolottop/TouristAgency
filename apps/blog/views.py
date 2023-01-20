from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.blog.models import Blog
from apps.gallery.models import Gallery

# Create your views here.
def blog(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    blog = Blog.objects.all()
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'blog':blog,
        'gallery':gallery,
        
    }
    return render(request, 'blog.html', context)

def blog_detail(request,id):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    blog = Blog.objects.get(id = id)
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'blog':blog,
        'gallery':gallery,
        
    }
    return render(request, 'blog-details.html', context)