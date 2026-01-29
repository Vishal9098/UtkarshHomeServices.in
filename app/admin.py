# from django.contrib import admin
# from .models import (
#     Customer,
#     Cart,
#     OrderPlaced,
#     Product,
#     ServicePrice
# )

# # --------------------
# # CUSTOMER
# # --------------------
# @admin.register(Customer)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'mobile', 'address', 'created_at']


# # --------------------
# # SERVICE PRICE INLINE
# # --------------------
# class ServicePriceInline(admin.TabularInline):
#     model = ServicePrice
#     extra = 1


# # --------------------
# # PRODUCT
# # --------------------
# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'category', 'is_service']
#     list_filter = ['is_service', 'category']
#     inlines = [ServicePriceInline]   # 👈 YAHI MAGIC HAI


# # --------------------
# # CART
# # --------------------
# @admin.register(Cart)
# class CartModelAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'session_key',
#         'product',
#         'get_service_option',
#         'quantity',
#         'get_price'
#     ]

#     def get_service_option(self, obj):
#         if obj.service_price:
#             return obj.service_price.option
#         return '-'
#     get_service_option.short_description = 'Service Option'

#     def get_price(self, obj):
#         return obj.unit_price()
#     get_price.short_description = 'Unit Price'


# # --------------------
# # ORDER
# # --------------------
# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'customer',
#         'product',
#         'get_service_option',
#         'quantity',
#         'price',
#         'status',
#         'ordered_at'
#     ]

#     def get_service_option(self, obj):
#         if obj.service_price:
#             return obj.service_price.option
#         return '-'
#     get_service_option.short_description = 'Service Option'


from django.contrib import admin
from .models import (
    Customer,
    Cart,
    OrderPlaced,
    Product,
    ServicePrice
)

# --------------------
# CUSTOMER
# --------------------
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'address', 'created_at']


# --------------------
# SERVICE PRICE INLINE
# --------------------
class ServicePriceInline(admin.TabularInline):
    model = ServicePrice
    extra = 1


# --------------------
# PRODUCT
# --------------------
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'is_service']
    list_filter = ['is_service', 'category']
    inlines = [ServicePriceInline]   # 👈 YAHI MAGIC HAI


# --------------------
# CART
# --------------------
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'session_key',
        'product',
        'get_service_option',
        'quantity',
        'get_price'
    ]

    def get_service_option(self, obj):
        if obj.service_price:
            return obj.service_price.option
        return '-'
    get_service_option.short_description = 'Service Option'

    def get_price(self, obj):
        return obj.unit_price()
    get_price.short_description = 'Unit Price'


# --------------------
# ORDER
# --------------------
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'product',
        'get_service_option',
        'quantity',
        'price',
        'status',
        'ordered_at'
    ]

    def get_service_option(self, obj):
        if obj.service_price:
            return obj.service_price.option
        return '-'
    get_service_option.short_description = 'Service Option'
