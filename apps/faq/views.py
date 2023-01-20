from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.settings.models import Settings
from apps.contacts.models import Contacts
from apps.faq.models import Faq,Question

# Create your views here.
def faq(request):
    settings = Settings.objects.latest('id')
    contact = Contacts.objects.latest('id')
    faq = Faq.objects.all()
    if request.method == "POST":
        name  = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')
        Question.objects.create(name = name, email = email, question = question)

        send_mail(
            f'{question}',
            f'Здравствуйте {name}, спасибо за отклик. Мы скоро свями свяжемся, пожалуйста будьте на связи. Ваш вопрос: {question}, Ваша почта: {email}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('faq')
    
    context = {
        'settings':settings,
        'contact':contact,
        'faq':faq,
    }
    return render(request, 'faq.html', context)

