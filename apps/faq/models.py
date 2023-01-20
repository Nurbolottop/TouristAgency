from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=255,verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемый вопрос"