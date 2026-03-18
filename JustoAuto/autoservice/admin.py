from django.contrib import admin

from .models import Car, OrderLine, Order, Service

class OrderAdminInline(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'car']
    inlines = [OrderAdminInline]

class Automobiliai(admin.ModelAdmin):
    list_display = ['make', 'model', 'client_name', 'license_plate', 'vin_code']


admin.site.register(Car, Automobiliai)
admin.site.register(OrderLine)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service)




