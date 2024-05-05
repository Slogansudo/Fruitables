
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Country, City, Address, Customers

# Register your models here.


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name', 'created_date')
    search_fields = ('id', 'name', 'created_date')
    list_filter = ('id', 'name', 'created_date')
    ordering = ('name',)


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links =('id', 'name', 'created_date')
    search_fields = ('id', 'name', 'created_date')
    list_filter = ('id', 'name', 'created_date')
    ordering = ('id', 'name',)


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name', 'created_date')
    search_fields = ('id', 'name', 'created_date')
    list_filter = ('id', 'name', 'created_date')
    ordering = ('id', 'name')


@admin.register(Customers)
class CustomersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email',)
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email')
    search_fields = ('id', 'first_name', 'last_name', 'username',)
    list_filter = ('id', 'first_name', 'last_name',)
    ordering = ('id', 'first_name',)
