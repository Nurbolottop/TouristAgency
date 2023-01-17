from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_image = models.ImageField(upload_to="blog", verbose_name="Фотография ")
    blog_name = models.CharField(max_length=255,verbose_name="Название")
    blog_description = models.TextField(verbose_name="Описание")
    blog_type = models.CharField(max_length=255,verbose_name="Тип")
    blog_time = models.DateTimeField(auto_now_add = True,blank=True, null=True)
    
    def __str__(self):
        return self.blog_name
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    