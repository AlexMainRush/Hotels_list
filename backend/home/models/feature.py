from django.db import models


class Feature(models.Model):
    name_feature = models.CharField(max_length=200, null=True, verbose_name='Заголовок причины')
    num_feature = models.CharField(max_length=200, null=True, verbose_name='Номер причины')
    text_feature = models.TextField(null=True, verbose_name='Текст причины')

    def __str__(self):
        return f'{self.name_feature}'

    class Meta:
        verbose_name = "Причина"
        verbose_name_plural = "Причины"
