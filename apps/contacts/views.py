from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.contacts.models import Contacts,Contact_detail
from apps.settings.models import Settings
from apps.gallery.models import Gallery

# Create your views here.
def contacts(request):
    contact = Contacts.objects.latest('id')
    settings = Settings.objects.latest('id')
    gallery = Gallery.objects.all()
    if request.method == "POST":
        name  = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact_detail.objects.create(name = name, email = email, message = message)

        send_mail(
            f'{message}',
            f'Здравствуйте {name}, спасибо за отклик. Мы скоро свями свяжемся, пожалуйста будьте на связи. Ваше сообщение: {message}, Ваша почта: {email}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('contacts')
    context = {
        'contact': contact,
        'settings':settings,
        'gallery':gallery,
        
    }
    
    return render(request, 'contact.html', context)