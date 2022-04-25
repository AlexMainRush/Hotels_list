from django.db import models


class Recommendations(models.Model):
    name_rec = models.CharField(max_length=200, null=True, verbose_name='Заголовок рекомендации')
    text_rec = models.TextField(null=True, verbose_name='Текст рекомендации')

    def __str__(self):
        return f'{self.name_rec}'

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"
