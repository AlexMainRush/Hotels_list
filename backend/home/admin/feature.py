from django.contrib import admin

from ..models.feature import Feature


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass
