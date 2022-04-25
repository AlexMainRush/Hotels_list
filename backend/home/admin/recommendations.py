from django.contrib import admin

from ..models.recommendations import Recommendations


@admin.register(Recommendations)
class RecommendationsAdmin(admin.ModelAdmin):
    pass
