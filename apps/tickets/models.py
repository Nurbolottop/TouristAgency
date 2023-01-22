from django.db import models

# Create your models here.
class Tickets(models.Model):
    image_ticket = models.ImageField(upload_to="tickets", verbose_name="Фотография")
    price_ticket = models.CharField(max_length=255,verbose_name="Цена")
    title = models.CharField(max_length=255,verbose_name="Название")
    description_ticket = models.TextField(verbose_name="Описание")
    first_image = models.ImageField(upload_to="tickets",verbose_name="Первая дополнительная фотография")
    second_image = models.ImageField(upload_to="tickets",verbose_name="Вторая дополнительная фотография")
    address_ticket = models.CharField(max_length=255,verbose_name="Место назначения")
    departur_time = models.CharField(max_length=255,verbose_name="Время отправления")
    return_time = models.CharField(max_length=255,verbose_name="Время возврата")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"

class Comment(models.Model):
    name = models.CharField(max_length=255,verbose_name="Имя")
    email = models.EmailField(verbose_name="Почта")
    message = models.TextField(verbose_name="Коментарий")
    post = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name="post_comment")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created",)