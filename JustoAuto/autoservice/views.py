from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.db.models import Q
from django.views.generic.edit import FormMixin
from .forms import OrderReviewForm, UserUpdateForm, ProfileUpdateForm
from .models import Car, Service, Order, OrderLine
from django.views import generic


def index(request):
    num_masinu = Car.objects.all().count()
    num_paslaug = Service.objects.all().count()
    num_atlikta = Order.objects.filter(status='4').count()

    # Papildome kintamuoju num_visits, įkeliame jį į kontekstą.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_masinu': num_masinu,
        'num_paslaug': num_paslaug,
        'num_atlikta': num_atlikta,
        'num_visits': num_visits,
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

class OrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'
    form_class = OrderReviewForm

    def get_success_url(self):
        return reverse ('order', kwargs={"pk": self.object.pk})


    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad knyga bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.order = self.get_object()
        form.instance.reviewer = self.request.user
        form.save()
        return super().form_valid(form)


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

class MyOrderInstanceListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "myorders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = UserUpdateForm
    template_name = "profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=...):
        return self.request.user

@login_required
def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        return redirect('profile')
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, template_name="profile.html", context=context)