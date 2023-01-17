from django.db import models

# Create your models here.
class Team(models.Model):
    team_image = models.ImageField(upload_to="team", verbose_name= " Фотография")
    team_name = models.CharField(max_length=255,verbose_name="Ф.И.О")
    team_work = models.CharField(max_length=244,verbose_name="Должность")
    team_email = models.EmailField(verbose_name="Почта")
    team_instagram = models.URLField(verbose_name="Instagram", blank=True, null=True)
    team_facebook = models.URLField(verbose_name="Facebook", blank=True, null=True)
    team_whatsapp = models.URLField(verbose_name="WhatsApp", blank=True, null=True)
    
    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"
        
        