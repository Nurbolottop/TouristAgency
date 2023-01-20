from django.db import models

# Create your models here.
class About(models.Model):
    image_1 = models.ImageField(upload_to="about",verbose_name="Первая фотография о нас")
    image_2 = models.ImageField(upload_to="about",verbose_name="Вторая фотография о нас")
    video = models.URLField(verbose_name="Ссылка на видео")
    image_video = models.ImageField(upload_to="about", verbose_name="Обложка для видео")
    about = models.TextField(verbose_name="О нас и что мы предлагаем")
    
    def __str__(self):
        return self.about
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class AboutNumber(models.Model):
    oput = models.CharField(max_length=255,verbose_name="Oпыт", )
    person = models.CharField(max_length=255,verbose_name="Сотрудники")
    client = models.CharField(max_length=255,verbose_name="Клиентов")
    
    def __str__(self):
        return self.oput
    
    class Meta:
        verbose_name = "Мы в цифрах"
        verbose_name_plural = "Мы в цифрах"
        
        