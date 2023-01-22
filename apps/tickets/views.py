from django.shortcuts import render,redirect
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.tickets.models import Tickets,Comment
from apps.gallery.models import Gallery
from django.db.models import Q

# Create your views here.
def tickets(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    tickets = Tickets.objects.all()
    gallery = Gallery.objects.all()
    
    context = {
        'settings':settings,
        'contact':contact,
        'tickets':tickets,
        'gallery':gallery,
        
    }
    return render(request, 'destination.html', context)

def tickets_detail(request,id):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    tickets = Tickets.objects.get(id = id)
    gallery = Gallery.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        comment = Comment.objects.create(name = name,email = email, message = message,post = tickets)
        return redirect('tickets_detail' , tickets.id)
    context = {
        'settings':settings,
        'contact':contact,
        'tickets':tickets,
        'gallery':gallery,
        
    }
    return render(request, 'destination-details.html', context)

def ticket_search(request):
    product = Tickets.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    gallery = Gallery.objects.all()
    search_key = request.GET.get('key')
    if search_key:
        product  = Tickets.objects.filter(Q(title__icontains =search_key))
    context= {
        'settings': settings,
        'product':product,
        'contact':contact,
        'gallery':gallery,
    }
    return render(request, 'ticket_search.html', context)