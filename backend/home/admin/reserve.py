from django.contrib import admin
from ..models import ReserveHome


@admin.register(ReserveHome)
class ReserveHomeAdmin(admin.ModelAdmin):
    list_display = ('res_entry_date', 'res_depart_date', 'res_adult', 'res_child', 'res_created_at')
    readonly_fields = ('res_created_at',)
