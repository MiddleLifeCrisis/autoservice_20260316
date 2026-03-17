from django.contrib import admin

from .models import Car, OrderLine, Order, Service

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline]

admin.site.register(Car)
admin.site.register(OrderLine)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service)




