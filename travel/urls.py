"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from apps.settings.views import index
from apps.tours.views import tour,tour_detail,tour_search
from apps.contacts.views import contacts
from apps.blog.views import blog_detail,blog,blog_search
from apps.team.views import teams
from apps.tickets.views import tickets,tickets_detail,ticket_search
from apps.review.views import review
from apps.faq.views import faq
from apps.about.views import about
from apps.gallery.views import gallery


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('tours/', tour, name="tour"),
    path('tours_detail/<int:id>/', tour_detail, name="tour_detail"),
    path('contacts/', contacts, name="contacts"),
    path('blog/', blog, name="blog"),
    path('blog_detail/<int:id>/', blog_detail, name="blog_detail"),
    path('blog/', blog, name="blog"),
    path('teams/', teams, name="teams"),
    path('tickets/', tickets, name="tickets"),
    path('tickets_detail/<int:id>/', tickets_detail, name="tickets_detail"),
    path('review/', review, name = "review"),
    path('faq/', faq, name="faq"),
    path('about/', about, name="about"),
    path('gallery/', gallery, name="gallery"),
    path('ticket/search/', ticket_search, name="ticket_search"),
    path('blog/search/', blog_search, name="blog_search"),
    path('tour/search/', tour_search, name="tour_search"),
    
    
    
    
    
    
    
]
urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)