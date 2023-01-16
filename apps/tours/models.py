from django.db import models

# Create your models here.
class Tours(models.Model):
    image_tour = models.ImageField(upload_to="Tours", verbose_name="Фотография тура")
    name_tour = models.CharField(max_length=255,verbose_name="Название тура")
    
    description_tour = models.TextField(verbose_name="Описание тура")
    time_tour = models.CharField(max_length=255,verbose_name="Время тура")
    price_tour =models.CharField(max_length=255,verbose_name="Стоимость тура")
    
    def __str__(self):
        return self.name_tour
    
    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
        
class TourDetail(models.Model):
    toures = models.ForeignKey(
        Tours,
        on_delete=models.CASCADE,
        related_name="tourse",
        verbose_name="Туры"
        )
    type_tour = models.CharField(max_length=255,verbose_name="Тип тура")
    group_size_tour = models.CharField(max_length=255,verbose_name="Размер группы")
    first_image_tour = models.ImageField(upload_to="tours_image")
    second_image_tour = models.ImageField(upload_to="tours_image")
    destination_tour = models.CharField(max_length=255,verbose_name="Место назначения")
    depature_tour = models.CharField(max_length=255,verbose_name="Отъезд")
    departure_time_tour = models.CharField(max_length=255,verbose_name="Время отправления")
    return_time_tour = models.CharField(max_length=255,verbose_name="Время возврата")
    included_tour = models.TextField(verbose_name="Включено")
    excluded_tour = models.TextField(verbose_name="Исключенно")
    accommodation_tour = models.CharField(max_length=255,verbose_name="Оценка жилья")
    transport_tour = models.CharField(max_length=255,verbose_name="Оценка транспорта")
    comfort_tour = models.CharField(max_length=255,verbose_name="Оценка комфорта")
    hospitality_tour = models.CharField(max_length=255,verbose_name="Оценка гостеприимства")
    food_tour = models.CharField(max_length=255,verbose_name="Оценка еды")
    
    def __str__(self):
        return self.destination_tour
    
    class Meta:
        verbose_name = "Информация про тур"
        verbose_name_plural = "Информация про туры"
        
        