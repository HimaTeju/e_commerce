from django.contrib import admin
from .models import Item, Cart, CartItem, Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_price')

admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)