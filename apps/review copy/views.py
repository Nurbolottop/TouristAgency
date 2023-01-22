from django.shortcuts import render,redirect
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.review.models import Review
from apps.gallery.models import Gallery

# Create your views here.
def review(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    gallery = Gallery.objects.all()
    
    if request.method == "POST":
        name_user = request.POST.get('name_user')
        email_user = request.POST.get('email_user')
        message_user = request.POST.get('message_user')
        product = Review.objects.create( name_user = name_user, email_user = email_user, message_user = message_user)
        return redirect('index')
    context = {
        'settings':settings,
        'contact':contact,
        'gallery':gallery,
        
    }
    return render(request, 'review.html', context)