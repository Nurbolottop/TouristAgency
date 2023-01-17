from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.blog.models import Blog

# Create your views here.
def blog(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    blog = Blog.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'blog':blog,
    }
    return render(request, 'blog.html', context)