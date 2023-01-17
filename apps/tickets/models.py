from django.db import models

# Create your models here.
class Tickets(models.Model):
    image_ticket = models.ImageField(upload_to="tickets", verbose_name="Фотография")
    name_ticket = models.CharField(max_length=255,verbose_name="Название")
    description_ticket = models.TextField(verbose_name="Описание")
    first_image = models.ImageField(upload_to="tickets",verbose_name="Первая дополнительная фотография")
    second_image = models.ImageField(upload_to="tickets",verbose_name="Вторая дополнительная фотография")
    address_ticket = models.CharField(max_length=255,verbose_name="Место назначения")
    departur_time = models.CharField(max_length=255,verbose_name="Время отправления")
    return_time = models.CharField(max_length=255,verbose_name="Время возврата")
    
    def __str__(self):
        return self.name_ticket
    
    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"
        