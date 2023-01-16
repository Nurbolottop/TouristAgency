from django.shortcuts import render
from apps.settings.models import Settings
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')

    context = {
        'settings':settings
    }
    return render(request, 'index3.html', context)