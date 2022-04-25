from django.conf import settings
from django.db import models
from garpix_notify.models import Notify
from garpix_page.models import BasePage

from .feature import Feature
from .recommendations import Recommendations
from ..forms import ReserveHomeForm


class HomePage(BasePage):
    first_name = models.CharField(max_length=255, null=True)
    second_name = models.CharField(max_length=255, null=True)
    feature = models.ManyToManyField(Feature, verbose_name='Причины',
                                     related_name='features_names', blank=True)
    recommendations = models.ManyToManyField(Recommendations, verbose_name='Причины',
                                             related_name='recommendations_names', blank=True)
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context_all = {
            'all_r': Recommendations.objects.values(),
            'all_f': Feature.objects.values(),
            'res_form': ReserveHomeForm(),
        }
        context.update(context_all)

        # print(context)
        if request.method == 'POST':
            form = ReserveHomeForm(request.POST)
            print(form.data)
            print(form.is_valid())
            print(request.POST.dict())
            if form.is_valid():
                # form.save()
                reserve = form.save()
                Notify.send(settings.FEEDBACK_EVENT, {
                    'reserve': reserve,
                }, email='reserve@test.ru')
                context.update({
                    'res_form': form,
                })
        return context

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Homes"
        ordering = ("-created_at",)
