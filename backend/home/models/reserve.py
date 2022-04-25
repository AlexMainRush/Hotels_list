from django.db import models


class ReserveHome(models.Model):
    res_entry_date = models.CharField(max_length=50, verbose_name='Дата заезда')
    res_depart_date = models.CharField(max_length=50, verbose_name='Дата выезда')
    res_adult = models.IntegerField(verbose_name='Взрослые')
    res_child = models.IntegerField(verbose_name='Дети')
    res_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.res_entry_date

    class Meta:
        ordering = ('-res_created_at',)
