from django.shortcuts import render,redirect
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.review.models import Review

# Create your views here.
def review(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    if request.method == "POST":
        name_user = request.POST.get('name_user')
        email_user = request.POST.get('email_user')
        message_user = request.POST.get('message_user')
        product = Review.objects.create( name_user = name_user, email_user = email_user, message_user = message_user)
        return redirect('index')
    context = {
        'settings':settings,
        'contact':contact,
    }
    return render(request, 'review.html', context)