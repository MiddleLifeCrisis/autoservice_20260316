from django.db import models

class Service(models.Model):
    name = models.CharField(verbose_name="Paslaugos pav.")
    price = models.DecimalField(verbose_name="Paslaugos kaina, EUR",
                                max_digits=10,
                                decimal_places=2)

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

    def __str__(self):
        return f"{self.name}"

class OrderLine(models.Model):
    order = models.ForeignKey (to='Order', on_delete=models.SET_NULL, verbose_name="Užsakymas",
                               null=True, blank=True)
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, verbose_name="Paslauga",
                                null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Užsakomas kiekis", default=1)
    def line_sum(self):
        return self.quantity * self.service.price

    class Meta:
        verbose_name = 'Užsakymo eilutė'
        verbose_name_plural = 'Užsakymo eilutės'

    def __str__(self):
        return f"{self.order} {self.service} {self.quantity} {self.line_sum()}"

class Order(models.Model):
    date = models.DateField(null=True, blank=True, verbose_name="Data")
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Automobilis")

    def total_cost(self):
        eilutes = self.orderline_set.all()
        suma = sum(line.line_sum() for line in eilutes)

        return suma


    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

    def __str__(self):
        return f"{self.car} {self.date}"

class Car(models.Model):
    make = models.CharField(verbose_name="Brand", max_length=50)
    model = models.CharField(verbose_name="Model", max_length=50)
    license_plate = models.CharField(verbose_name="Valstybinis numeris")
    vin_code = models.CharField(verbose_name="VIN number")
    client_name = models.CharField(verbose_name="Kliento vardas ir pavardė")

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

    def __str__(self):
        return f"{self.make}-{self.license_plate}:{self.client_name}"

