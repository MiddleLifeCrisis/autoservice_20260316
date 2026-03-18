from django.contrib import admin

from .models import Car, OrderLine, Order, Service

class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'car']




admin.site.register(Car)
admin.site.register(OrderLine)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service)




