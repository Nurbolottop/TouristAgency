from django.db import models

# Create your models here.
class Contacts(models.Model):
    image_contact_site = models.ImageField(upload_to="contact",verbose_name="Фотография для страницы Контакты")
    email_site =models.EmailField(verbose_name="Почта")
    phone_site = models.CharField(max_length=255,verbose_name="Тел.ном")
    address_site = models.CharField(max_length=255,verbose_name="Адрес")
    maps_site = models.URLField(verbose_name="Адрес на карте")
    instagram_site = models.URLField(verbose_name="Instagram",blank=True, null=True)
    facebook_site = models.URLField(verbose_name="Fcebook",blank=True, null=True)
    youtube_site = models.URLField(verbose_name="Youtube",blank=True, null=True)
    whatsapp_site = models.URLField(verbose_name="WhatsApp",blank=True, null=True)
    
    def __str__(self):
        return self.email_site
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    