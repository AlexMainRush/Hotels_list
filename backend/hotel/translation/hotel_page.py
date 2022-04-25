from modeltranslation.translator import TranslationOptions, register
from ..models import HotelPage


@register(HotelPage)
class HotelPageTranslationOptions(TranslationOptions):
    pass
