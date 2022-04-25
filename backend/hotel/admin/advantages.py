from ..models.advantages import Advantages
from django.contrib import admin


@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
    pass
