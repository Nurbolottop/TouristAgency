from django.db import models

# Create your models here.
class Ticket_tours(models.Model):
    country = models.CharField(max_length=255,verbose_name="Страна")
    
    
    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = "Страну"
        verbose_name_plural = "Страны"
        
class Ticket_toursDetail(models.Model):
    countres = models.ForeignKey(
        Ticket_tours,
        on_delete= models.CASCADE,
        related_name="countres",
        verbose_name="Страны"
    )
    city = models.CharField(max_length=255,verbose_name="Город")
    
    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = "Город"
        verbose_name = "Города"
        
class Travel(models.Model):
    travel = models.CharField(max_length=255,verbose_name="Тип путешествия")
    
    def __str__(self):
        return self.travel
    
    class Meta:
        verbose_name = "Тип путешествия"