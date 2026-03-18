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
    list_filter = ['client_name', 'make', 'model']

    fieldsets = [
        ('Savininko informacija', {
            'fields': ('client_name',)
        }),
        ('Automobilio duomenys', {
            'fields': ('make', 'model', 'license_plate', 'vin_code'),
            'description': 'Pagrindinė techninė informacija apie transporto priemonę.'
        }),
    ]


class Paslaugos(admin.ModelAdmin):
    list_display = ['name', 'price']

admin.site.register(Car, Automobiliai)
admin.site.register(OrderLine)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, Paslaugos)




