from django.shortcuts import render
from apps.settings.models import Settings
from apps.tours.models import Tours
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    tour = Tours.objects.all()

    context = {
        'settings':settings,
        'tour':tour,
        
    }
    return render(request, 'index3.html', context)