from django.db import models

# Create your models here.
class Review(models.Model):
    image_user = models.ImageField(upload_to="users_reciew",verbose_name="Фотграфия")
    name_user = models.CharField(max_length=255,verbose_name="Имя")
    email_user = models.EmailField(verbose_name="Почта")
    message_user = models.TextField(verbose_name="Сообщение")
    
    def __str__(self):
        return self.name_user
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    