from django.contrib import admin

from logistic.models import Stock, Product, StockProduct


# Register your models here.


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    pass
