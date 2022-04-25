from django.db import models


class Advantages(models.Model):
    name_advantage = models.CharField(max_length=50, verbose_name='Наименование преимущества', null=True)

    def __str__(self):
        return self.name_advantage

    class Meta:
        verbose_name = "Преимущество гостиницы"
        verbose_name_plural = "Преимущества гостиниц"
