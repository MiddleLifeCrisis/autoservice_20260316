from django.contrib import admin

from .models import Car, OrderLine, Order, Service

class OrderAdminInline(admin.TabularInline):
    model = OrderLine
    fields = ['service', 'quantity', 'line_sum']  # Štai čia tavo stulpeliai!
    readonly_fields = ['line_sum']  # Būtina, kad rodytų metodą
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'car', 'total_cost']
    readonly_fields = ['total_cost']
    inlines = [OrderAdminInline]

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'service', 'quantity', 'line_sum']

class Automobiliai(admin.ModelAdmin):
    list_display = ['make', 'model', 'client_name', 'license_plate', 'vin_code']
    list_filter = ['client_name', 'make', 'model']
    search_fields = ['license_plate', 'vin_code', 'client_name']

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
# admin.site.register(OrderLine)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, Paslaugos)
admin.site.register(OrderLine, OrderLineAdmin)




