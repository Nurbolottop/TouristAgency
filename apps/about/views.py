from django.shortcuts import render
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.blog.models import Blog
from apps.about.models import About, AboutNumber
from apps.blog.models import Blog
from apps.team.models import Team
from apps.review.models import Review

# Create your views here.
def about(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    numder = AboutNumber.objects.latest('id')
    about = About.objects.latest('id')
    blog = Blog.objects.all()
    team = Team.objects.all()
    review = Review.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'numder':numder,
        'about':about,
        'blog':blog,
        'team':team,
        'review':review,
        
        
    }
    return render(request, 'about.html', context)
