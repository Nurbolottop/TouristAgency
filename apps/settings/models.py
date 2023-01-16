from django.db import models

# Create your models here.
class Settings(models.Model):
    logo_site = models.ImageField(upload_to="logo_site", verbose_name="Логотип")
    name_site = models.CharField(max_length=255,verbose_name="Название сайта")
    description_site = models.TextField(verbose_name="Описание сайта")

    def __str__(self):
        return self.name_site

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"