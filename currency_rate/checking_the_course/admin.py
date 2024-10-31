from django.contrib import admin

from .models import СourseRequest


@admin.register(СourseRequest)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('request_date', 'rate')
    search_fields = ('request_date',)
