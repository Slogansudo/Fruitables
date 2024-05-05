
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Billing
# Register your models here.


@admin.register(Billing)
class BillingAdmin(ImportExportModelAdmin):
    list_display = ('id', 'payment_type', 'comments_text', 'created_date')
    list_display_links = ('id', 'payment_type', 'created_date')
    search_fields = ('id', 'payment_type',)
    list_filter = ('id', 'payment_type',)
    ordering = ('created_date',)

    def comments_text(self, obj):
        return obj.comments[:15]
