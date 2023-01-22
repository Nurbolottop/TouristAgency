from django.shortcuts import render,redirect
from django.db.models import Q

from apps.tours.models import Tours,Comment
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.gallery.models import Gallery

# Create your views here.

def tour(request):
    tour = Tours.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'tour':tour,
        'contact': contact,
        'gallery':gallery,
        
    }
    return render(request,'package.html',context)

def tour_detail(request,id):
    tour = Tours.objects.get(id = id)   
    contact = Contacts.objects.latest('id')
    gallery = Gallery.objects.all()
    random_tour = Tours.objects.all().order_by('?')
    settings = Settings.objects.latest('id')
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        comment = Comment.objects.create(name = name,email = email, message = message,post = tour )
        return redirect('tour_detail' , tour.id)

    context = {
        'settings':settings,
        'tour':tour,
        'contact': contact,
        'gallery':gallery,
        'random_tour':random_tour,
    }
    return render(request,'package-details.html',context)

def tour_search(request):
    product = Tours.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    gallery = Gallery.objects.all()
    search_key = request.GET.get('key')
    if search_key:
        product  = Tours.objects.filter(Q(title__icontains =search_key))
    context= {
        'settings': settings,
        'product':product,
        'contact':contact,
        'gallery':gallery,
    }
    return render(request, 'tour_search.html', context)