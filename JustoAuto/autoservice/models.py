from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField
from django.core.paginator import Paginator

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
    order = models.ForeignKey (to='Order', on_delete=models.SET_NULL, verbose_name="Užsakymas", related_name='eilutes',
                               null=True, blank=True)
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, verbose_name="Paslauga", related_name='paslaugos',
                                null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Užsakomas kiekis", default=1)
    def line_sum(self):
        return self.quantity * self.service.price

    line_sum.short_description = "Suma, €"

    class Meta:
        verbose_name = 'Užsakymo eilutė'
        verbose_name_plural = 'Užsakymo eilutės'

    def __str__(self):
        return f"{self.order} {self.service} {self.quantity} {self.line_sum()}"

class Order(models.Model):
    date = models.DateField(null=True, blank=True, verbose_name="Data")
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Automobilis")
    client = models.ForeignKey(to=User, verbose_name="Klientas", on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateField(null=True, blank=True)

    def total_cost(self):
        eilutes = self.eilutes.all()
        suma = 0
        for line in eilutes:
            viena_suma = line.line_sum()
            suma = suma + viena_suma
        return suma

    total_cost.short_description = "Suma VISO, €"

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

    ORDER_STATUS = (
        ('1', 'Priimtas'),
        ('2', 'Vykdomas'),
        ('3', 'Laukia detalių'),
        ('4', 'Baigtas'),
    )

    status = models.CharField(verbose_name="Status", max_length=1, choices=ORDER_STATUS, blank=True, default="d")

    def is_overdue(self):
        return self.due_back and timezone.now().date() > self.due_back

    def __str__(self):
        return f"{self.car}"

class Car(models.Model):
    make = models.CharField(verbose_name="Brand", max_length=50)
    model = models.CharField(verbose_name="Model", max_length=50)
    license_plate = models.CharField(verbose_name="Valstybinis numeris")
    vin_code = models.CharField(verbose_name="VIN number")
    client_name = models.CharField(verbose_name="Kliento vardas ir pavardė")
    photo = models.ImageField(upload_to="car_photo", null=True, blank=True)
    description = HTMLField(default="")

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

    def __str__(self):
        return f"{self.make} - {self.license_plate}"

class OrderReview(models.Model):
    order = models.ForeignKey(to=Order,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='reviews')
    reviewer = models.ForeignKey(to=User,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-date_created']
