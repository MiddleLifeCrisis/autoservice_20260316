from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Service, Order, OrderLine


def index(request):
    num_masinu = Car.objects.all().count()
    num_paslaug = Service.objects.all().count()
    num_atlikta = Order.objects.filter(status='4').count()


    context = {
        'num_masinu': num_masinu,
        'num_paslaug': num_paslaug,
        'num_atlikta': num_atlikta,
    }

    return render(request, template_name="index.html", context=context)