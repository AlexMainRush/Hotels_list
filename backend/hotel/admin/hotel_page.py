from ..models.hotel_page import HotelPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(HotelPage)
class HotelPageAdmin(BasePageAdmin):
    pass
