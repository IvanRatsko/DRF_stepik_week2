from django.contrib import admin

from .models import ProductSet, Recipient, Order


class ProductSetAdmin(admin.ModelAdmin):
    pass


class RecipientAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductSet, ProductSetAdmin)
admin.site.register(Recipient, RecipientAdmin)
admin.site.register(Order, OrderAdmin)
