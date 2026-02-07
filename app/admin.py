from django.contrib import admin
from .models import Customer, Product, ServicePrice, Cart, OrderPlaced


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'address')


class ServicePriceInline(admin.TabularInline):
    model = ServicePrice
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_service')
    inlines = [ServicePriceInline]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'get_service_option', 'quantity')

    def get_service_option(self, obj):
        return obj.service_price.option if obj.service_price else '-'
    get_service_option.short_description = 'Service Option'


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'status')
    list_filter = ('status',)

from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')


