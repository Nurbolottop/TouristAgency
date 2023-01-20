from django.contrib import admin
from apps.about.models import About, AboutNumber
# Register your models here.
admin.site.register(AboutNumber)
admin.site.register(About)