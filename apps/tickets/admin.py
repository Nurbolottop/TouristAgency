from django.contrib import admin
from apps.tickets.models import Tickets,Comment
# Register your models here.
admin.site.register(Tickets)
admin.site.register(Comment)
