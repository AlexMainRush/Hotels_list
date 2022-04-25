from django.db import models
from garpix_page.models import BasePage
from ..models.advantages import Advantages


class HotelPage(BasePage):
    name_hotel = models.CharField(max_length=255, verbose_name='Наименование гостиницы', null=True)
    advantages_hotel = models.ManyToManyField(Advantages, verbose_name='Преимущества отеля',
                                              related_name='advantages_tags', blank=True)
    TYPE_HOTEL = (
        ('H', 'Гостиница'),
        ('M', 'Мотель'),
        ('A', 'Апартаменты'),
    )
    type_hotel = models.CharField(max_length=1, choices=TYPE_HOTEL, default='M',
                                  verbose_name='Тип гостиницы', blank=True)  # можно было тоже сделать МЭНИтуМЭНИ и отдавать на список
    cost_hotel = models.IntegerField(verbose_name='Стоимость номера от', null=True)
    small_image_hotel = models.ImageField(verbose_name='Маленькое изображение гостиницы', null=True)
    template = 'pages/hotel.html'

    def __str__(self):
        return self.name_hotel

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
        ordering = ("-created_at",)
