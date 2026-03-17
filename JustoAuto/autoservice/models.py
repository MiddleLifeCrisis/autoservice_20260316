from django.db import models

class Service(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class OrderLine(models.Model):
    order = models.ForeignKey (to='Order', on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.order} {self.service} {self.quantity}"

class Order(models.Model):
    date = models.DateField(null=True, blank=True)
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL, null=True, blank=True)
    # service = models.ManyToManyField(to="Service", through='OrderLine')
    def __str__(self):
        return f"{self.car} {self.date}"

class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField()
    vin_code = models.CharField()
    client_name = models.CharField()

    def __str__(self):
        return f"{self.make} {self.client_name} {self.license_plate}"

