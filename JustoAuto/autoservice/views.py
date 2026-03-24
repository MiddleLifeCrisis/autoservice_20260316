from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.db.models import Q

Q

from .models import Car, Service, Order, OrderLine
from django.views import generic


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

def kainorastis(request):
    paslaugos = Service.objects.all() # Paima duomenis iš admine esančių paslaugų
    return render(request, 'kainorastis.html', {'paslaugos': paslaugos})

def about(request):
    return render(request, template_name="about.html")

def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        'cars': paged_cars,
    }
    print(cars)
    return render(request, template_name="cars.html", context=context)

def car(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, template_name="car.html", context={'car': car })

class OrderListView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'
    paginate_by = 3

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'

def search(request):
    query = request.GET.get('query')
    context = {
        "car_search_results": Car.objects.filter(Q (make__icontains=query) |
                                                 Q (model__icontains=query) |
                                                 Q (license_plate__icontains=query) |
                                                 Q (vin_code__icontains=query) |
                                                 Q (client_name=query)
                                                 ),
    }
    return render(request, template_name="search.html", context=context)