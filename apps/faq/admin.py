from django.contrib import admin
from apps.faq.models import Faq,Question
# Register your models here.

admin.site.register(Faq)
admin.site.register(Question)
