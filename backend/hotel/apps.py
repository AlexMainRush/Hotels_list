from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HotelConfig(AppConfig):
    name = 'hotel'
    verbose_name = _('Hotel')
