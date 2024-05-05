
from django.contrib import admin
from .models import Product, Category, Cart, Comment
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('title', 'created_date')
    list_display_links = ('title',)
    search_fields = ('id', 'title')
    list_filter = ('title',)
    ordering = ('title',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'price', 'price_type', 'rating', 'created_date')
    list_display_links = ('id', 'title', 'price', 'price_type', 'rating', 'created_date')
    search_fields = ('id', 'title', 'rating', 'price', 'price_type')
    list_filter = ('title', 'price')
    ordering = ('id', 'title')


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'text_xx', 'created_date')
    list_display_links =('id', 'text_xx', 'created_date')
    search_fields = ('id', 'created_date')
    list_filter = ('id', 'created_date')
    ordering = ('id',)

    def text_xx(self, obj):
        return obj.text[:10]


@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
    list_display = ('id', 'product_number', 'shipping_price', 'total_price', 'created_date')
    list_display_links = ('id', 'product_number', 'shipping_price')
    search_fields = ('id', 'product_number','created_date')
    list_filter = ('id', 'created_date')
    ordering = ('id', 'product_number',)

