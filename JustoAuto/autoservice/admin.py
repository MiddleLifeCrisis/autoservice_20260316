from django.contrib import admin

from .models import Car, OrderLine, Order, Service

admin.site.register(Car)
admin.site.register(OrderLine)
admin.site.register(Order)
admin.site.register(Service)


