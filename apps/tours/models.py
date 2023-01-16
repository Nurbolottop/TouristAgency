from django.db import models

# Create your models here.
class Tours(models.Model):
    image_tour = models.ImageField(upload_to="Tours", verbose_name="Фотография тура")
    name_tour = models.CharField(max_length=255,verbose_name="Название тура")