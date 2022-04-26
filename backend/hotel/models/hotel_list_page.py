from garpix_page.models import BaseListPage

from .advantages import Advantages
from .hotel_page import HotelPage


class HotelListPage(BaseListPage):
    paginate_by = 2
    template = 'pages/hotels.html'

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context_all = {
            'all_hotel': HotelPage.objects.values(),
            'all_adv': Advantages.objects.all()
        }
        context.update(context_all)
        return context

    class Meta:
        verbose_name = "HotelList"
        verbose_name_plural = "HotelLists"
        ordering = ('-created_at',)
